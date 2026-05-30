from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.session import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    customer_name: Mapped[str] = mapped_column(
        String,
    )

    product_name: Mapped[str] = mapped_column(
        String,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    pickup_date: Mapped[str] = mapped_column(
        String,
    )

    status: Mapped[str] = mapped_column(
        String,
        default="new",
    )