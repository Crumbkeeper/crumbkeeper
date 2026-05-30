from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.customer import Customer
from app.schemas.customer import (
    CustomerCreate,
    CustomerResponse,
    CustomerUpdate,
)

router = APIRouter()


@router.post(
    "/customers",
    response_model=CustomerResponse,
)
def create_customer(
    payload: CustomerCreate,
    db: Session = Depends(get_db),
):
    customer = Customer(**payload.model_dump())

    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer


@router.get(
    "/customers",
    response_model=list[CustomerResponse],
)
def list_customers(
    db: Session = Depends(get_db),
):
    return db.query(Customer).all()


@router.put(
    "/customers/{customer_id}",
    response_model=CustomerResponse,
)
def update_customer(
    customer_id: int,
    payload: CustomerUpdate,
    db: Session = Depends(get_db),
):
    customer = db.query(Customer).filter(
        Customer.id == customer_id
    ).first()

    for key, value in payload.model_dump().items():
        setattr(customer, key, value)

    db.commit()
    db.refresh(customer)

    return customer