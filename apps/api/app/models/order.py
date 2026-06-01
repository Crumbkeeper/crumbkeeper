from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.session import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    customer_name: Mapped[str] = mapped_column(String)
    product_name: Mapped[str] = mapped_column(String)
    quantity: Mapped[int] = mapped_column(default=1)
    pickup_date: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String, default="new")
    fulfillment_type: Mapped[str] = mapped_column(String, default="pickup")
    payment_status: Mapped[str] = mapped_column(String, default="pending")
    total_price: Mapped[float] = mapped_column(Float, default=0.0)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
