from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.ingredient import Ingredient
from app.schemas.ingredient import (
    IngredientCreate,
    IngredientResponse,
    IngredientUpdate,
)

router = APIRouter()


@router.post(
    "/ingredients",
    response_model=IngredientResponse,
)
def create_ingredient(
    payload: IngredientCreate,
    db: Session = Depends(get_db),
):
    ingredient = Ingredient(
        **payload.model_dump()
    )

    db.add(ingredient)
    db.commit()
    db.refresh(ingredient)

    return ingredient


@router.get(
    "/ingredients",
    response_model=list[IngredientResponse],
)
def list_ingredients(
    db: Session = Depends(get_db),
):
    return db.query(Ingredient).all()


@router.get(
    "/ingredients/{ingredient_id}",
    response_model=IngredientResponse,
)
def get_ingredient(
    ingredient_id: int,
    db: Session = Depends(get_db),
):
    ingredient = (
        db.query(Ingredient)
        .filter(
            Ingredient.id == ingredient_id
        )
        .first()
    )

    if not ingredient:
        raise HTTPException(
            status_code=404,
            detail="Ingredient not found",
        )

    return ingredient


@router.put(
    "/ingredients/{ingredient_id}",
    response_model=IngredientResponse,
)
def update_ingredient(
    ingredient_id: int,
    payload: IngredientUpdate,
    db: Session = Depends(get_db),
):
    ingredient = (
        db.query(Ingredient)
        .filter(
            Ingredient.id == ingredient_id
        )
        .first()
    )

    if not ingredient:
        raise HTTPException(
            status_code=404,
            detail="Ingredient not found",
        )

    for key, value in payload.model_dump().items():
        setattr(
            ingredient,
            key,
            value,
        )

    db.commit()
    db.refresh(ingredient)

    return ingredient


@router.delete(
    "/ingredients/{ingredient_id}"
)
def delete_ingredient(
    ingredient_id: int,
    db: Session = Depends(get_db),
):
    ingredient = (
        db.query(Ingredient)
        .filter(
            Ingredient.id == ingredient_id
        )
        .first()
    )

    if not ingredient:
        raise HTTPException(
            status_code=404,
            detail="Ingredient not found",
        )

    db.delete(ingredient)
    db.commit()

    return {
        "deleted": True,
        "id": ingredient_id,
    }
