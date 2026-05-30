from pydantic import BaseModel


class InventoryBase(BaseModel):
    product_id: int
    item_name: str
    category: str = "ingredient"
    quantity_on_hand: float = 0
    projected_depletion: float = 0
    unit: str = "units"
    reorder_threshold: float = 0
    low_stock: bool = False


class InventoryCreate(InventoryBase):
    pass


class InventoryUpdate(InventoryBase):
    pass


class InventoryResponse(InventoryBase):
    id: int

    class Config:
        from_attributes = True