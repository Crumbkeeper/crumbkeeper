from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.core.security import hash_password
from app.core.security import verify_password
from app.core.tokens import create_access_token
from app.db.session import get_db
from app.models.user import User
from app.schemas.auth import RegisterRequest
from app.schemas.auth import TokenResponse
from app.schemas.auth import UserResponse


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register", response_model=UserResponse)
def register(
    payload: RegisterRequest,
    db: Session = Depends(get_db),
):
    existing_user = (
        db.query(User)
        .filter(User.email == payload.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    user = User(
        email=payload.email,
        password_hash=hash_password(payload.password),
        bakery_name=payload.bakery_name,
        role="owner",
        is_active=True,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@router.post("/login", response_model=TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = (
        db.query(User)
        .filter(User.email == form_data.username)
        .first()
    )

    if not user or not verify_password(
        form_data.password,
        user.password_hash,
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    if not user.is_active:
        raise HTTPException(
            status_code=403,
            detail="User account is inactive",
        )

    token = create_access_token(user.email)

    return TokenResponse(
        access_token=token
    )


@router.get("/me", response_model=UserResponse)
def get_me(
    user: User = Depends(get_current_user),
):
    return user
