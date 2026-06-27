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
