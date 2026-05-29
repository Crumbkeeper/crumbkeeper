from fastapi import APIRouter
from fastapi import Depends

from app.api.deps import get_current_user
from app.schemas.auth import LoginRequest
from app.schemas.auth import TokenResponse
from app.core.tokens import create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest):
    token = create_access_token(payload.email)

    return TokenResponse(
        access_token=token
    )


@router.get("/me")
def get_me(
    user=Depends(get_current_user),
):
    return user
