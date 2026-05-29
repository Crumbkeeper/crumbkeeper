from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.core.tokens import decode_access_token


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
):
    try:
        payload = decode_access_token(token)

        email = payload.get("sub")

        if not email:
            raise HTTPException(
                status_code=401,
                detail="Invalid token",
            )

        return {
            "email": email
        }

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication",
        )
