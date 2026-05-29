from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.recipe import Recipe
from app.schemas.recipe import (
    RecipeCreate,
    RecipeResponse,
    RecipeScaleRequest,
    RecipeScaleResponse,
    RecipeUpdate,
)

router = APIRouter()


@router.post("/recipes", response_model=RecipeResponse)
def create_recipe(
    payload: RecipeCreate,
    db: Session = Depends(get_db),
):
    recipe = Recipe(**payload.model_dump())

    db.add(recipe)
    db.commit()
    db.refresh(recipe)

    return recipe


@router.get("/recipes", response_model=list[RecipeResponse])
def list_recipes(
    db: Session = Depends(get_db),
):
    return db.query(Recipe).all()


@router.get("/recipes/{recipe_id}", response_model=RecipeResponse)
def get_recipe(
    recipe_id: int,
    db: Session = Depends(get_db),
):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()

    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    return recipe


@router.put("/recipes/{recipe_id}", response_model=RecipeResponse)
def update_recipe(
    recipe_id: int,
    payload: RecipeUpdate,
    db: Session = Depends(get_db),
):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()

    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    for key, value in payload.model_dump().items():
        setattr(recipe, key, value)

    recipe.version += 1

    db.commit()
    db.refresh(recipe)

    return recipe


@router.post("/recipes/{recipe_id}/scale", response_model=RecipeScaleResponse)
def scale_recipe(
    recipe_id: int,
    payload: RecipeScaleRequest,
    db: Session = Depends(get_db),
):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()

    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    factor = payload.target_yield / recipe.yield_count

    return RecipeScaleResponse(
        flour_grams=recipe.flour_grams * factor,
        water_grams=recipe.water_grams * factor,
        starter_grams=recipe.starter_grams * factor,
        salt_grams=recipe.salt_grams * factor,
        target_yield=payload.target_yield,
    )
