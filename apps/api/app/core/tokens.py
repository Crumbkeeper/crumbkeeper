from datetime import datetime
from datetime import timedelta
from typing import Optional

from jose import jwt


SECRET_KEY = "crumbkeeper-super-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(
    subject: str,
    expires_delta: Optional[timedelta] = None,
):
    expire = datetime.utcnow() + (
        expires_delta or timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    payload = {
        "sub": subject,
        "exp": expire,
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def decode_access_token(token: str):
    return jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM],
    )
