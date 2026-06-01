from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.session import Base


class DemandForecast(Base):
    __tablename__ = "demand_forecasts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    category: Mapped[str] = mapped_column(String)
    projected_units: Mapped[int] = mapped_column(default=0)
    confidence_score: Mapped[float] = mapped_column(Float, default=0.0)


class SalesTrendSnapshot(Base):
    __tablename__ = "sales_trend_snapshots"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    trend_value: Mapped[float] = mapped_column(Float, default=0.0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class GrowthTarget(Base):
    __tablename__ = "growth_targets"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    target_type: Mapped[str] = mapped_column(String)
    target_value: Mapped[float] = mapped_column(Float)


class InventoryProjection(Base):
    __tablename__ = "inventory_projections"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    ingredient_name: Mapped[str] = mapped_column(String)
    projected_remaining: Mapped[float] = mapped_column(Float)


class ForecastAlert(Base):
    __tablename__ = "forecast_alerts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    alert_type: Mapped[str] = mapped_column(String)
    message: Mapped[str] = mapped_column(String)
