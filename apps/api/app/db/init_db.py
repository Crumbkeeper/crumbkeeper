from sqlalchemy.orm import Session

from app.db.session import Base
from app.db.session import SessionLocal
from app.db.session import engine

import app.db.base
from app.models.bakery import Bakery
from app.models.ingredient import Ingredient
from app.models.recipe import Recipe
from app.models.recipe_ingredient import RecipeIngredient


def seed_defaults(db: Session):
    bakery = db.query(Bakery).first()

    if bakery is None:
        return

    if db.query(Ingredient).count() == 0:
        flour = Ingredient(
            bakery_id=bakery.id,
            name="Bread Flour",
            category="Flour",
            unit="g",
            current_stock=25000,
            reorder_threshold=5000,
        )

        water = Ingredient(
            bakery_id=bakery.id,
            name="Water",
            category="Liquid",
            unit="g",
            current_stock=100000,
            reorder_threshold=10000,
        )

        salt = Ingredient(
            bakery_id=bakery.id,
            name="Salt",
            category="Seasoning",
            unit="g",
            current_stock=5000,
            reorder_threshold=500,
        )

        db.add_all([flour, water, salt])
        db.commit()

    recipe = db.query(Recipe).first()

    if recipe and db.query(RecipeIngredient).count() == 0:
        ingredients = db.query(Ingredient).all()

        for ingredient in ingredients:
            amount = {
                "Bread Flour": 500,
                "Water": 350,
                "Salt": 10,
            }.get(ingredient.name)

            if amount is None:
                continue

            db.add(
                RecipeIngredient(
                    recipe_id=recipe.id,
                    ingredient_id=ingredient.id,
                    quantity=amount,
                    unit="g",
                )
            )

        db.commit()


def init_db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        seed_defaults(db)
    finally:
        db.close()
