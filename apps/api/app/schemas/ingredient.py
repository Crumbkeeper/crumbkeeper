from pydantic import BaseModel


class IngredientBase(BaseModel):
    bakery_id: int = 1

    name: str

    category: str = "Other"

    unit: str = "g"

    current_stock: float = 0

    reorder_threshold: float = 0

    cost_per_unit: float = 0

    vendor: str | None = None

    notes: str | None = None

    active: bool = True


class IngredientCreate(IngredientBase):
    pass


class IngredientUpdate(IngredientBase):
    pass


class IngredientResponse(IngredientBase):
    id: int

    class Config:
        from_attributes = True
