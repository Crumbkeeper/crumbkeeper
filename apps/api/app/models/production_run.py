from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.session import Base


class ProductionRun(Base):
    __tablename__ = "production_runs"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    task_name: Mapped[str] = mapped_column(
        String,
    )

    scheduled_time: Mapped[str] = mapped_column(
        String,
    )

    linked_order_id: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String,
        default="scheduled",
    )