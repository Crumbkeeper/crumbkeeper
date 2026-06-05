from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.inventory import Inventory
from app.schemas.inventory import (
    InventoryCreate,
    InventoryResponse,
    InventoryUpdate,
)

router = APIRouter()


def apply_low_stock_status(item: Inventory) -> Inventory:
    item.low_stock = item.quantity_on_hand <= item.reorder_threshold
    return item


@router.post(
    "/inventory",
    response_model=InventoryResponse,
)
def create_inventory(
    payload: InventoryCreate,
    db: Session = Depends(get_db),
):
    item = Inventory(**payload.model_dump())
    apply_low_stock_status(item)

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
    return db.query(Inventory).order_by(Inventory.item_name.asc()).all()


@router.get(
    "/inventory/{item_id}",
    response_model=InventoryResponse,
)
def get_inventory_item(
    item_id: int,
    db: Session = Depends(get_db),
):
    item = db.query(Inventory).filter(Inventory.id == item_id).first()

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Inventory item not found",
        )

    return item


@router.put(
    "/inventory/{item_id}",
    response_model=InventoryResponse,
)
def update_inventory_item(
    item_id: int,
    payload: InventoryUpdate,
    db: Session = Depends(get_db),
):
    item = db.query(Inventory).filter(Inventory.id == item_id).first()

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Inventory item not found",
        )

    for key, value in payload.model_dump().items():
        setattr(item, key, value)

    apply_low_stock_status(item)

    db.commit()
    db.refresh(item)

    return item


@router.delete(
    "/inventory/{item_id}",
)
def delete_inventory_item(
    item_id: int,
    db: Session = Depends(get_db),
):
    item = db.query(Inventory).filter(Inventory.id == item_id).first()

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Inventory item not found",
        )

    db.delete(item)
    db.commit()

    return {
        "deleted": True,
        "id": item_id,
    }
