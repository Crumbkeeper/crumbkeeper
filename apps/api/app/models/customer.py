from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.session import Base


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String,
    )

    email: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    preferred_pickup_day: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    favorite_products: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    bake_preferences: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    last_order_date: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )