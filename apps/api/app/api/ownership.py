from fastapi import Depends
from fastapi import HTTPException

from app.api.deps import get_current_user


def verify_bakery_owner(
    bakery_email: str,
    user=Depends(get_current_user),
):
    if user["email"] != bakery_email:
        raise HTTPException(
            status_code=403,
            detail="Not authorized for this bakery",
        )

    return user
