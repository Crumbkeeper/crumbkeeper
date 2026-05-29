from pydantic import BaseModel


class PaginationParams(BaseModel):
    skip: int = 0
    limit: int = 25


class PaginatedResponse(BaseModel):
    total: int
    skip: int
    limit: int
    items: list
