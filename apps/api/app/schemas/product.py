from pydantic import BaseModel


class ProductBase(BaseModel):
    bakery_id: int
    recipe_id: int | None = None
    name: str
    category: str
    description: str | None = None
    sku: str | None = None
    default_price: float = 0
    lead_time_hours: int = 24
    max_daily_quantity: int = 10
    order_cutoff_hours: int = 24
    available_days: str | None = None
    active: bool = True


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True