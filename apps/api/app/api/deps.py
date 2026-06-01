from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.tokens import decode_access_token
from app.db.session import get_db
from app.models.user import User


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    try:
        payload = decode_access_token(token)
        email = payload.get("sub")

        if not email:
            raise HTTPException(
                status_code=401,
                detail="Invalid token",
            )

        user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if not user or not user.is_active:
            raise HTTPException(
                status_code=401,
                detail="Invalid authentication",
            )

        return user

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication",
        )


def require_owner(
    user: User = Depends(get_current_user),
) -> User:
    if user.role != "owner":
        raise HTTPException(
            status_code=403,
            detail="Owner access required",
        )

    return user
