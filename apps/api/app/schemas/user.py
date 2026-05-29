from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    bakery_name: str | None = None


class UserResponse(BaseModel):
    id: int
    email: str
    bakery_name: str | None = None

    class Config:
        from_attributes = True
