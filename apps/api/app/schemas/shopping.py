from pydantic import BaseModel


class ShoppingItemBase(BaseModel):
    inventory_item_id: int | None = None
    item_name: str
    quantity_needed: float = 0
    unit: str = "units"
    status: str = "needed"
    source: str = "manual"
    notes: str | None = None


class ShoppingItemCreate(ShoppingItemBase):
    pass


class ShoppingItemUpdate(ShoppingItemBase):
    pass


class ShoppingItemResponse(ShoppingItemBase):
    id: int

    class Config:
        from_attributes = True
