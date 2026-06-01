from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.websocket import manager
from app.db.session import get_db
from app.models.order import Order
from app.schemas.order import OrderCreate
from app.schemas.order import OrderResponse
from app.schemas.order import OrderUpdate


router = APIRouter()


@router.post("/orders", response_model=OrderResponse)
async def create_order(
    payload: OrderCreate,
    db: Session = Depends(get_db),
):
    order = Order(**payload.model_dump())

    db.add(order)
    db.commit()
    db.refresh(order)

    await manager.broadcast(
        "order_created",
        {"id": order.id, "status": order.status},
    )

    return order


@router.get("/orders", response_model=list[OrderResponse])
def list_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()


@router.get("/orders/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order


@router.put("/orders/{order_id}", response_model=OrderResponse)
async def update_order(
    order_id: int,
    payload: OrderUpdate,
    db: Session = Depends(get_db),
):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    for key, value in payload.model_dump().items():
        setattr(order, key, value)

    db.commit()
    db.refresh(order)

    await manager.broadcast(
        "order_updated",
        {"id": order.id, "status": order.status},
    )

    return order
