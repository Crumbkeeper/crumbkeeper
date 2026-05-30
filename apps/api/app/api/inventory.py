from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.inventory import Inventory
from app.schemas.inventory import (
    InventoryCreate,
    InventoryResponse,
)

router = APIRouter()


@router.post(
    "/inventory",
    response_model=InventoryResponse,
)
def create_inventory(
    payload: InventoryCreate,
    db: Session = Depends(get_db),
):
    item = Inventory(**payload.model_dump())

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


@router.get(
    "/inventory",
    response_model=list[InventoryResponse],
)
def list_inventory(
    db: Session = Depends(get_db),
):
    return db.query(Inventory).all()