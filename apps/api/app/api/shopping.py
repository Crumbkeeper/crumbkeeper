from datetime import datetime

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.inventory import Inventory
from app.models.shopping import ShoppingItem
from app.schemas.shopping import (
    ShoppingItemCreate,
    ShoppingItemResponse,
    ShoppingItemUpdate,
)

router = APIRouter()


def sync_inventory_shopping_items(db: Session) -> None:
    low_stock_items = (
        db.query(Inventory)
        .filter(Inventory.available_quantity <= Inventory.reorder_threshold)
        .all()
    )

    for inventory_item in low_stock_items:
        existing = (
            db.query(ShoppingItem)
            .filter(
                ShoppingItem.inventory_item_id == inventory_item.id,
                ShoppingItem.status != "purchased",
            )
            .first()
        )

        needed_amount = max(
            inventory_item.reorder_threshold - inventory_item.available_quantity,
            inventory_item.projected_depletion,
            0,
        )

        if existing:
            existing.item_name = inventory_item.item_name
            existing.quantity_needed = needed_amount
            existing.unit = inventory_item.unit
            existing.source = "inventory"
            existing.status = "needed"
        else:
            db.add(
                ShoppingItem(
                    inventory_item_id=inventory_item.id,
                    item_name=inventory_item.item_name,
                    quantity_needed=needed_amount,
                    unit=inventory_item.unit,
                    status="needed",
                    source="inventory",
                )
            )

    db.commit()


@router.get(
    "/shopping-list",
    response_model=list[ShoppingItemResponse],
)
def list_shopping_items(
    db: Session = Depends(get_db),
):
    sync_inventory_shopping_items(db)

    return (
        db.query(ShoppingItem)
        .order_by(ShoppingItem.status.asc(), ShoppingItem.item_name.asc())
        .all()
    )


@router.post(
    "/shopping-list",
    response_model=ShoppingItemResponse,
)
def create_shopping_item(
    payload: ShoppingItemCreate,
    db: Session = Depends(get_db),
):
    item = ShoppingItem(**payload.model_dump())

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


@router.put(
    "/shopping-list/{item_id}",
    response_model=ShoppingItemResponse,
)
def update_shopping_item(
    item_id: int,
    payload: ShoppingItemUpdate,
    db: Session = Depends(get_db),
):
    item = db.query(ShoppingItem).filter(ShoppingItem.id == item_id).first()

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Shopping item not found",
        )

    previous_status = item.status

    for key, value in payload.model_dump().items():
        setattr(item, key, value)

    if item.status == "purchased" and previous_status != "purchased":
        item.purchased_at = datetime.utcnow()

        if item.inventory_item_id is not None:
            inventory_item = (
                db.query(Inventory)
                .filter(Inventory.id == item.inventory_item_id)
                .first()
            )

            if inventory_item:
                inventory_item.quantity_on_hand += item.quantity_needed
                inventory_item.available_quantity = (
                    inventory_item.quantity_on_hand - inventory_item.reserved_quantity
                )
                inventory_item.low_stock = (
                    inventory_item.available_quantity <= inventory_item.reorder_threshold
                )
    else:
        item.purchased_at = None

    db.commit()
    db.refresh(item)

    return item


@router.delete(
    "/shopping-list/{item_id}",
)
def delete_shopping_item(
    item_id: int,
    db: Session = Depends(get_db),
):
    item = db.query(ShoppingItem).filter(ShoppingItem.id == item_id).first()

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Shopping item not found",
        )

    db.delete(item)
    db.commit()

    return {
        "deleted": True,
        "id": item_id,
    }
