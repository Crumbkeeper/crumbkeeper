from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.recipe import Recipe
from app.schemas.recipe import (
    RecipeCreate,
    RecipeResponse,
)

router = APIRouter()


@router.post(
    "/recipes",
    response_model=RecipeResponse,
)
def create_recipe(
    payload: RecipeCreate,
    db: Session = Depends(get_db),
):
    recipe = Recipe(
        name=payload.name,
        category=payload.category,
    )

    db.add(recipe)
    db.commit()
    db.refresh(recipe)

    return recipe


@router.get(
    "/recipes",
    response_model=list[RecipeResponse],
)
def list_recipes(
    db: Session = Depends(get_db),
):
    return db.query(Recipe).all()
