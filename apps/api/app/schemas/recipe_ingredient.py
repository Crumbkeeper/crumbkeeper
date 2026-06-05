from pydantic import BaseModel


class RecipeIngredientBase(BaseModel):
    recipe_id: int
    ingredient_id: int
    quantity: float
    unit: str = "g"


class RecipeIngredientCreate(
    RecipeIngredientBase
):
    pass


class RecipeIngredientUpdate(
    RecipeIngredientBase
):
    pass


class RecipeIngredientResponse(
    RecipeIngredientBase
):
    id: int

    class Config:
        from_attributes = True
