from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.inventory import Inventory
from app.schemas.inventory import (
    InventoryConsume,
    InventoryCreate,
    InventoryReserve,
    InventoryResponse,
    InventoryUpdate,
)

router = APIRouter()


def apply_inventory_status(item: Inventory) -> Inventory:
    item.available_quantity = item.quantity_on_hand - item.reserved_quantity
    item.low_stock = item.available_quantity <= item.reorder_threshold
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
    apply_inventory_status(item)

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

    apply_inventory_status(item)

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


@router.post(
    "/inventory/{item_id}/reserve",
    response_model=InventoryResponse,
)
def reserve_inventory(
    item_id: int,
    payload: InventoryReserve,
    db: Session = Depends(get_db),
):
    item = db.query(Inventory).filter(Inventory.id == item_id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Inventory item not found")

    if payload.quantity <= 0:
        raise HTTPException(status_code=400, detail="Reservation quantity must be greater than zero")

    apply_inventory_status(item)

    if payload.quantity > item.available_quantity:
        raise HTTPException(status_code=400, detail="Insufficient available inventory")

    item.reserved_quantity += payload.quantity
    apply_inventory_status(item)

    db.commit()
    db.refresh(item)

    return item


@router.post(
    "/inventory/{item_id}/consume",
    response_model=InventoryResponse,
)
def consume_inventory(
    item_id: int,
    payload: InventoryConsume,
    db: Session = Depends(get_db),
):
    item = db.query(Inventory).filter(Inventory.id == item_id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Inventory item not found")

    if payload.quantity <= 0:
        raise HTTPException(status_code=400, detail="Consumption quantity must be greater than zero")

    if payload.quantity > item.reserved_quantity:
        raise HTTPException(status_code=400, detail="Cannot consume more than reserved inventory")

    item.reserved_quantity -= payload.quantity
    item.quantity_on_hand -= payload.quantity
    apply_inventory_status(item)

    db.commit()
    db.refresh(item)

    return item
