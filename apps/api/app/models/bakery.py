from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.session import Base


class Bakery(Base):
    __tablename__ = "bakeries"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String,
        unique=True,
        index=True,
    )

    owner_email: Mapped[str] = mapped_column(
        String,
        unique=True,
        index=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    products = relationship("Product", back_populates="bakery")
    ingredients = relationship("Ingredient", back_populates="bakery")
    settings = relationship(
        "BakerySettings",
        back_populates="bakery",
        uselist=False,
    )
