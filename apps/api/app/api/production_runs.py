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
        {"id": run.id, "status": run.status},
    )

    return run


@router.get("/production-runs", response_model=list[ProductionRunResponse])
def list_production_runs(db: Session = Depends(get_db)):
    return db.query(ProductionRun).all()


@router.get("/production-runs/{run_id}", response_model=ProductionRunResponse)
def get_production_run(run_id: int, db: Session = Depends(get_db)):
    run = db.query(ProductionRun).filter(ProductionRun.id == run_id).first()

    if not run:
        raise HTTPException(status_code=404, detail="Production run not found")

    return run


@router.put("/production-runs/{run_id}", response_model=ProductionRunResponse)
async def update_production_run(
    run_id: int,
    payload: ProductionRunUpdate,
    db: Session = Depends(get_db),
):
    run = db.query(ProductionRun).filter(ProductionRun.id == run_id).first()

    if not run:
        raise HTTPException(status_code=404, detail="Production run not found")

    for key, value in payload.model_dump().items():
        setattr(run, key, value)

    db.commit()
    db.refresh(run)

    await manager.broadcast(
        "production_updated",
        {"id": run.id, "status": run.status},
    )

    return run
