from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.ingredient import Ingredient
from app.models.recipe import Recipe
from app.models.recipe_ingredient import RecipeIngredient

from app.schemas.recipe_ingredient import (
    RecipeIngredientCreate,
    RecipeIngredientResponse,
    RecipeIngredientUpdate,
)

router = APIRouter()


def recalculate_recipe_totals(
    recipe_id: int,
    db: Session,
):
    recipe = (
        db.query(Recipe)
        .filter(Recipe.id == recipe_id)
        .first()
    )

    if not recipe:
        return

    flour = 0.0
    water = 0.0
    starter = 0.0
    salt = 0.0

    links = (
        db.query(RecipeIngredient)
        .filter(
            RecipeIngredient.recipe_id == recipe_id
        )
        .all()
    )

    for link in links:
        ingredient = (
            db.query(Ingredient)
            .filter(
                Ingredient.id == link.ingredient_id
            )
            .first()
        )

        if not ingredient:
            continue

        category = ingredient.category

        if category == "Flour":
            flour += link.quantity

        elif category == "Water":
            water += link.quantity

        elif category == "Starter":
            starter += link.quantity

        elif category == "Salt":
            salt += link.quantity

    recipe.flour_grams = flour
    recipe.water_grams = water
    recipe.starter_grams = starter
    recipe.salt_grams = salt

    recipe.dough_weight = (
        flour
        + water
        + starter
        + salt
    )

    db.commit()


@router.post(
    "/recipe-ingredients",
    response_model=RecipeIngredientResponse,
)
def create_recipe_ingredient(
    payload: RecipeIngredientCreate,
    db: Session = Depends(get_db),
):
    item = RecipeIngredient(
        **payload.model_dump()
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    recalculate_recipe_totals(
        item.recipe_id,
        db,
    )

    return item


@router.get(
    "/recipe-ingredients",
    response_model=list[
        RecipeIngredientResponse
    ],
)
def list_recipe_ingredients(
    db: Session = Depends(get_db),
):
    return (
        db.query(RecipeIngredient)
        .all()
    )


@router.put(
    "/recipe-ingredients/{item_id}",
    response_model=RecipeIngredientResponse,
)
def update_recipe_ingredient(
    item_id: int,
    payload: RecipeIngredientUpdate,
    db: Session = Depends(get_db),
):
    item = (
        db.query(RecipeIngredient)
        .filter(
            RecipeIngredient.id == item_id
        )
        .first()
    )

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Recipe ingredient not found",
        )

    for key, value in (
        payload.model_dump().items()
    ):
        setattr(
            item,
            key,
            value,
        )

    db.commit()
    db.refresh(item)

    recalculate_recipe_totals(
        item.recipe_id,
        db,
    )

    return item


@router.delete(
    "/recipe-ingredients/{item_id}"
)
def delete_recipe_ingredient(
    item_id: int,
    db: Session = Depends(get_db),
):
    item = (
        db.query(RecipeIngredient)
        .filter(
            RecipeIngredient.id == item_id
        )
        .first()
    )

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Recipe ingredient not found",
        )

    recipe_id = item.recipe_id

    db.delete(item)
    db.commit()

    recalculate_recipe_totals(
        recipe_id,
        db,
    )

    return {
        "deleted": True,
        "id": item_id,
    }
