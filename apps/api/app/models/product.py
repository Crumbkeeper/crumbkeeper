from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.session import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    bakery_id: Mapped[int] = mapped_column(
        ForeignKey("bakeries.id"),
        nullable=False,
    )

    recipe_id: Mapped[int | None] = mapped_column(
        ForeignKey("recipes.id"),
        nullable=True,
    )

    name: Mapped[str] = mapped_column(String, index=True)

    category: Mapped[str] = mapped_column(String)

    description: Mapped[str | None] = mapped_column(String, nullable=True)

    sku: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
        unique=True,
    )

    default_price: Mapped[float] = mapped_column(Float, default=0.0)

    lead_time_hours: Mapped[int] = mapped_column(Integer, default=24)

    max_daily_quantity: Mapped[int] = mapped_column(Integer, default=10)

    order_cutoff_hours: Mapped[int] = mapped_column(Integer, default=24)

    available_days: Mapped[str | None] = mapped_column(String, nullable=True)

    active: Mapped[bool] = mapped_column(Boolean, default=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    bakery = relationship("Bakery", back_populates="products")
    inventory = relationship("Inventory", back_populates="product", uselist=False)
    recipe = relationship("Recipe")