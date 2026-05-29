from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.production_run import ProductionRun
from app.schemas.production_run import (
    ProductionRunCreate,
    ProductionRunResponse,
)

router = APIRouter()


@router.post(
    "/production-runs",
    response_model=ProductionRunResponse,
)
def create_production_run(
    payload: ProductionRunCreate,
    db: Session = Depends(get_db),
):
    run = ProductionRun(
        name=payload.name,
        status=payload.status,
    )

    db.add(run)
    db.commit()
    db.refresh(run)

    return run


@router.get(
    "/production-runs",
    response_model=list[ProductionRunResponse],
)
def list_production_runs(
    db: Session = Depends(get_db),
):
    return db.query(
        ProductionRun
    ).all()
