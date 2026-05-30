from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.order import Order
from app.schemas.order import (
    OrderCreate,
    OrderResponse,
)

router = APIRouter()


@router.post(
    "/orders",
    response_model=OrderResponse,
)
def create_order(
    payload: OrderCreate,
    db: Session = Depends(get_db),
):
    order = Order(**payload.model_dump())

    db.add(order)
    db.commit()
    db.refresh(order)

    return order


@router.get(
    "/orders",
    response_model=list[OrderResponse],
)
def list_orders(
    db: Session = Depends(get_db),
):
    return db.query(Order).all()