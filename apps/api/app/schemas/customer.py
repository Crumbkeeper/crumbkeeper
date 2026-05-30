from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: str
    email: str | None = None
    phone: str | None = None
    preferred_pickup_day: str | None = None
    favorite_products: str | None = None
    bake_preferences: str | None = None
    notes: str | None = None


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(CustomerBase):
    pass


class CustomerResponse(CustomerBase):
    id: int

    class Config:
        from_attributes = True