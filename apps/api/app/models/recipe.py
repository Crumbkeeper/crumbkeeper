from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.session import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String, index=True)

    category: Mapped[str | None] = mapped_column(String, nullable=True)

    flour_grams: Mapped[float] = mapped_column(Float, default=0)

    water_grams: Mapped[float] = mapped_column(Float, default=0)

    starter_grams: Mapped[float] = mapped_column(Float, default=0)

    salt_grams: Mapped[float] = mapped_column(Float, default=0)

    yield_count: Mapped[int] = mapped_column(Integer, default=1)

    dough_weight: Mapped[float] = mapped_column(Float, default=0)

    bulk_fermentation_hours: Mapped[float] = mapped_column(Float, default=0)

    cold_retard_hours: Mapped[float] = mapped_column(Float, default=0)

    bake_temperature: Mapped[int] = mapped_column(Integer, default=450)

    bake_duration_minutes: Mapped[int] = mapped_column(Integer, default=45)

    version: Mapped[int] = mapped_column(Integer, default=1)

    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    ingredient_links = relationship(
        "RecipeIngredient",
        back_populates="recipe",
    )
