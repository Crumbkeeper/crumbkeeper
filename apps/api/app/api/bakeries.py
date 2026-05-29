from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.bakery import Bakery
from app.schemas.bakery import (
    BakeryCreate,
    BakeryResponse,
)

router = APIRouter()


@router.post(
    "/bakeries",
    response_model=BakeryResponse,
)
def create_bakery(
    payload: BakeryCreate,
    db: Session = Depends(get_db),
):
    bakery = Bakery(
        name=payload.name,
        owner_email=payload.owner_email,
        phone=payload.phone,
    )

    db.add(bakery)
    db.commit()
    db.refresh(bakery)

    return bakery


@router.get(
    "/bakeries",
    response_model=list[BakeryResponse],
)
def list_bakeries(
    db: Session = Depends(get_db),
):
    return db.query(Bakery).all()
