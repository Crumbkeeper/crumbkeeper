from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.session import Base


class ProductionRun(Base):
    __tablename__ = "production_runs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    task_name: Mapped[str] = mapped_column(String)
    scheduled_time: Mapped[str] = mapped_column(String)
    linked_order_id: Mapped[int | None] = mapped_column(nullable=True)
    stage: Mapped[str] = mapped_column(String, default="prep")
    priority: Mapped[str] = mapped_column(String, default="normal")
    batch_size: Mapped[int] = mapped_column(default=1)
    dough_weight: Mapped[float] = mapped_column(Float, default=0.0)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String, default="scheduled")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
