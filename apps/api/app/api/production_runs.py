from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.websocket import manager
from app.db.session import get_db
from app.models.production_run import ProductionRun
from app.schemas.production_run import ProductionRunCreate
from app.schemas.production_run import ProductionRunResponse
from app.schemas.production_run import ProductionRunUpdate


router = APIRouter()


@router.post("/production-runs", response_model=ProductionRunResponse)
async def create_production_run(
    payload: ProductionRunCreate,
    db: Session = Depends(get_db),
):
    run = ProductionRun(**payload.model_dump())

    db.add(run)
    db.commit()
    db.refresh(run)

    await manager.broadcast(
        "production_created",
        {
            "id": run.id,
            "status": run.status,
        },
    )

    return run


@router.get("/production-runs", response_model=list[ProductionRunResponse])
def list_production_runs(
    db: Session = Depends(get_db),
):
    return db.query(ProductionRun).all()


@router.get("/production-runs/{run_id}", response_model=ProductionRunResponse)
def get_production_run(
    run_id: int,
    db: Session = Depends(get_db),
):
    run = (
        db.query(ProductionRun)
        .filter(ProductionRun.id == run_id)
        .first()
    )

    if not run:
        raise HTTPException(
            status_code=404,
            detail="Production run not found",
        )

    return run


@router.put("/production-runs/{run_id}", response_model=ProductionRunResponse)
async def update_production_run(
    run_id: int,
    payload: ProductionRunUpdate,
    db: Session = Depends(get_db),
):
    run = (
        db.query(ProductionRun)
        .filter(ProductionRun.id == run_id)
        .first()
    )

    if not run:
        raise HTTPException(
            status_code=404,
            detail="Production run not found",
        )

    for key, value in payload.model_dump().items():
        setattr(run, key, value)

    db.commit()
    db.refresh(run)

    await manager.broadcast(
        "production_updated",
        {
            "id": run.id,
            "status": run.status,
        },
    )

    return run

from app.models.production_run import ProductionItem
from app.schemas.production_run import ProductionItemCreate
from app.schemas.production_run import ProductionItemResponse
from app.schemas.production_run import ProductionItemUpdate


@router.post(
    "/production-runs/{run_id}/items",
    response_model=ProductionItemResponse,
)
def create_production_item(
    run_id: int,
    payload: ProductionItemCreate,
    db: Session = Depends(get_db),
):
    run = (
        db.query(ProductionRun)
        .filter(ProductionRun.id == run_id)
        .first()
    )

    if not run:
        raise HTTPException(
            status_code=404,
            detail="Production run not found",
        )

    item_data = payload.model_dump()
    item_data["production_run_id"] = run_id

    item = ProductionItem(**item_data)

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


@router.get(
    "/production-runs/{run_id}/items",
    response_model=list[ProductionItemResponse],
)
def list_production_items(
    run_id: int,
    db: Session = Depends(get_db),
):
    run = (
        db.query(ProductionRun)
        .filter(ProductionRun.id == run_id)
        .first()
    )

    if not run:
        raise HTTPException(
            status_code=404,
            detail="Production run not found",
        )

    return (
        db.query(ProductionItem)
        .filter(ProductionItem.production_run_id == run_id)
        .all()
    )


@router.put(
    "/production-items/{item_id}",
    response_model=ProductionItemResponse,
)
def update_production_item(
    item_id: int,
    payload: ProductionItemUpdate,
    db: Session = Depends(get_db),
):
    item = (
        db.query(ProductionItem)
        .filter(ProductionItem.id == item_id)
        .first()
    )

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Production item not found",
        )

    for key, value in payload.model_dump().items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)

    return item


@router.delete("/production-items/{item_id}")
def delete_production_item(
    item_id: int,
    db: Session = Depends(get_db),
):
    item = (
        db.query(ProductionItem)
        .filter(ProductionItem.id == item_id)
        .first()
    )

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Production item not found",
        )

    db.delete(item)
    db.commit()

    return {"message": "Production item deleted"}

from datetime import datetime
from datetime import timedelta

from app.models.production_run import ProductionTemplateStage
from app.schemas.production_run import ProductionItemAdvanceStage


@router.post(
    "/production-items/{item_id}/advance",
    response_model=ProductionItemResponse,
)
async def advance_production_item_stage(
    item_id: int,
    payload: ProductionItemAdvanceStage,
    db: Session = Depends(get_db),
):
    item = (
        db.query(ProductionItem)
        .filter(ProductionItem.id == item_id)
        .first()
    )

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Production item not found",
        )

    item.current_stage_index = item.current_stage_index + 1
    item.stage_started_at = datetime.utcnow()

    next_stage = None

    if item.template_id is not None:
        next_stage = (
            db.query(ProductionTemplateStage)
            .filter(
                ProductionTemplateStage.template_id == item.template_id,
                ProductionTemplateStage.stage_order == item.current_stage_index,
            )
            .first()
        )

    if next_stage and next_stage.alert_after_minutes is not None:
        delay_minutes = payload.delay_minutes or next_stage.alert_after_minutes
        item.suggested_stage_end = item.stage_started_at + timedelta(
            minutes=delay_minutes,
        )
    elif payload.delay_minutes is not None:
        item.suggested_stage_end = item.stage_started_at + timedelta(
            minutes=payload.delay_minutes,
        )
    else:
        item.suggested_stage_end = None

    item.status = "active"

    db.commit()
    db.refresh(item)

    await manager.broadcast(
        "production_item_advanced",
        {
            "id": item.id,
            "production_run_id": item.production_run_id,
            "current_stage_index": item.current_stage_index,
            "status": item.status,
        },
    )

    return item


@router.get("/production-board")
def get_production_board(
    db: Session = Depends(get_db),
):
    runs = db.query(ProductionRun).all()

    board = []

    for run in runs:
        run_items = (
            db.query(ProductionItem)
            .filter(ProductionItem.production_run_id == run.id)
            .all()
        )

        items = []

        for item in run_items:
            current_stage = None

            if item.template_id is not None:
                current_stage = (
                    db.query(ProductionTemplateStage)
                    .filter(
                        ProductionTemplateStage.template_id == item.template_id,
                        ProductionTemplateStage.stage_order == item.current_stage_index,
                    )
                    .first()
                )

            items.append(
                {
                    "id": item.id,
                    "recipe_id": item.recipe_id,
                    "product_id": item.product_id,
                    "template_id": item.template_id,
                    "planned_quantity": item.planned_quantity,
                    "production_quantity": item.production_quantity,
                    "good_quantity": item.good_quantity,
                    "waste_quantity": item.waste_quantity,
                    "waste_reason": item.waste_reason,
                    "current_stage_index": item.current_stage_index,
                    "current_stage_name": current_stage.stage_name if current_stage else None,
                    "status": item.status,
                    "notes": item.notes,
                    "stage_started_at": item.stage_started_at,
                    "suggested_stage_end": item.suggested_stage_end,
                }
            )

        board.append(
            {
                "id": run.id,
                "name": run.name,
                "production_date": run.production_date,
                "status": run.status,
                "notes": run.notes,
                "items": items,
            }
        )

    return board

from app.schemas.production_run import ProductionItemComplete


@router.post(
    "/production-items/{item_id}/complete",
    response_model=ProductionItemResponse,
)
async def complete_production_item(
    item_id: int,
    payload: ProductionItemComplete,
    db: Session = Depends(get_db),
):
    item = (
        db.query(ProductionItem)
        .filter(ProductionItem.id == item_id)
        .first()
    )

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Production item not found",
        )

    item.good_quantity = payload.good_quantity
    item.waste_quantity = payload.waste_quantity
    item.waste_reason = payload.waste_reason
    item.status = "completed"
    item.completed_at = datetime.utcnow()
    item.suggested_stage_end = None

    if payload.notes is not None:
        item.notes = payload.notes

    db.commit()
    db.refresh(item)

    await manager.broadcast(
        "production_item_completed",
        {
            "id": item.id,
            "production_run_id": item.production_run_id,
            "status": item.status,
            "good_quantity": item.good_quantity,
            "waste_quantity": item.waste_quantity,
        },
    )

    return item
