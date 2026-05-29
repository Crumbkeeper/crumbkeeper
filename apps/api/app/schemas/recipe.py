from pydantic import BaseModel


class RecipeCreate(BaseModel):
    name: str
    category: str | None = None


class RecipeResponse(BaseModel):
    id: int
    name: str
    category: str | None = None

    class Config:
        from_attributes = True
