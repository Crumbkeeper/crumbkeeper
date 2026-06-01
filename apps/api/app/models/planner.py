from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.session import Base


class ProductionPlan(Base):
    __tablename__ = "production_plans"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    name: Mapped[str] = mapped_column(String)
    projected_hours: Mapped[float] = mapped_column(Float, default=0.0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class ProductionConflict(Base):
    __tablename__ = "production_conflicts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    conflict_type: Mapped[str] = mapped_column(String)
    severity: Mapped[str] = mapped_column(String)
    recommendation: Mapped[str] = mapped_column(String)


class ProductionRecommendation(Base):
    __tablename__ = "production_recommendations"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    message: Mapped[str] = mapped_column(String)
