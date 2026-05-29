from pydantic import BaseModel


class RecipeBase(BaseModel):
    name: str
    category: str | None = None
    flour_grams: float = 0
    water_grams: float = 0
    starter_grams: float = 0
    salt_grams: float = 0
    yield_count: int = 1
    dough_weight: float = 0
    bulk_fermentation_hours: float = 0
    cold_retard_hours: float = 0
    bake_temperature: int = 450
    bake_duration_minutes: int = 45
    notes: str | None = None


class RecipeCreate(RecipeBase):
    pass


class RecipeUpdate(RecipeBase):
    pass


class RecipeResponse(RecipeBase):
    id: int
    version: int

    class Config:
        from_attributes = True


class RecipeScaleRequest(BaseModel):
    target_yield: int


class RecipeScaleResponse(BaseModel):
    flour_grams: float
    water_grams: float
    starter_grams: float
    salt_grams: float
    target_yield: int
