from pydantic import BaseModel


class OrderBase(BaseModel):
    customer_name: str
    product_name: str
    quantity: int = 1
    pickup_date: str
    status: str = "new"


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderBase):
    pass


class OrderResponse(OrderBase):
    id: int

    class Config:
        from_attributes = True