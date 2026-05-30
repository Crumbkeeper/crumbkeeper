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


class Inventory(Base):
    __tablename__ = "inventory"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        nullable=False,
        unique=True,
    )

    item_name: Mapped[str] = mapped_column(
        String,
    )

    category: Mapped[str] = mapped_column(
        String,
        default="ingredient",
    )

    quantity_on_hand: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    projected_depletion: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    unit: Mapped[str] = mapped_column(
        String,
        default="units",
    )

    reorder_threshold: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    low_stock: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    last_updated: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    product = relationship("Product", back_populates="inventory")