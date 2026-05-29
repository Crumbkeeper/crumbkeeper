from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.session import Base


class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    bakery_id: Mapped[int] = mapped_column(
        ForeignKey("bakeries.id"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String,
        index=True,
    )

    unit: Mapped[str] = mapped_column(
        String,
        default="g",
    )

    cost_per_unit: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    vendor: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    active: Mapped[bool] = mapped_column(
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    bakery = relationship("Bakery", back_populates="ingredients")
    recipe_links = relationship("RecipeIngredient", back_populates="ingredient")
