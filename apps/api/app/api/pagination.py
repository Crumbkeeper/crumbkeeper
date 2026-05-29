from fastapi import Query

from app.schemas.pagination import PaginationParams


def get_pagination(
    skip: int = Query(0, ge=0),
    limit: int = Query(25, ge=1, le=100),
):
    return PaginationParams(
        skip=skip,
        limit=limit,
    )
