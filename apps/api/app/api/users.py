from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import User
from app.schemas.user import (
    UserCreate,
    UserResponse,
)

router = APIRouter()


@router.post(
    "/users",
    response_model=UserResponse,
)
def create_user(
    payload: UserCreate,
    db: Session = Depends(get_db),
):
    user = User(
        email=payload.email,
        bakery_name=payload.bakery_name,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@router.get(
    "/users",
    response_model=list[UserResponse],
)
def list_users(
    db: Session = Depends(get_db),
):
    return db.query(User).all()
