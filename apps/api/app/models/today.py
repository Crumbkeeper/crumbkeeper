from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.session import Base


class TodayTask(Base):
    __tablename__ = "today_tasks"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    task_name: Mapped[str] = mapped_column(String)
    priority: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String, default="pending")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class TodayAlert(Base):
    __tablename__ = "today_alerts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    alert_message: Mapped[str] = mapped_column(String)
    severity: Mapped[str] = mapped_column(String)
