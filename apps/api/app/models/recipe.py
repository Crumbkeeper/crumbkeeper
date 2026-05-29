from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.session import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String,
        index=True,
    )

    category: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    ingredient_links = relationship(
        "RecipeIngredient",
        back_populates="recipe",
    )
