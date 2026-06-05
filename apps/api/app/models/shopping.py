from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.session import Base


class ShoppingItem(Base):
    __tablename__ = "shopping_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    inventory_item_id: Mapped[int | None] = mapped_column(
        ForeignKey("inventory.id"),
        nullable=True,
    )

    item_name: Mapped[str] = mapped_column(String, index=True)

    quantity_needed: Mapped[float] = mapped_column(Float, default=0)

    unit: Mapped[str] = mapped_column(String, default="units")

    status: Mapped[str] = mapped_column(String, default="needed")

    source: Mapped[str] = mapped_column(String, default="manual")

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

    purchased_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    inventory_item = relationship("Inventory")
