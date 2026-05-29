from pydantic import BaseModel


class OrderCreate(BaseModel):
    status: str = "pending"


class OrderResponse(BaseModel):
    id: int
    status: str

    class Config:
        from_attributes = True
