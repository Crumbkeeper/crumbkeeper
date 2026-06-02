from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.session import Base


class MarketEvent(Base):
    __tablename__ = "market_events"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    name: Mapped[str] = mapped_column(String)
    event_date: Mapped[str] = mapped_column(String)
    location: Mapped[str | None] = mapped_column(String, nullable=True)
    expected_customers: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class MarketInventoryPlan(Base):
    __tablename__ = "market_inventory_plans"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    market_event_id: Mapped[int | None] = mapped_column(nullable=True)
    product_name: Mapped[str] = mapped_column(String)
    planned_units: Mapped[int] = mapped_column(Integer, default=0)
    expected_sell_through_percent: Mapped[float] = mapped_column(Float, default=0.0)


class EventForecast(Base):
    __tablename__ = "event_forecasts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    market_event_id: Mapped[int | None] = mapped_column(nullable=True)
    projected_revenue: Mapped[float] = mapped_column(Float, default=0.0)
    projected_units: Mapped[int] = mapped_column(Integer, default=0)
    risk_level: Mapped[str] = mapped_column(String, default="normal")


class SellThroughRecord(Base):
    __tablename__ = "sell_through_records"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    market_event_id: Mapped[int | None] = mapped_column(nullable=True)
    product_name: Mapped[str] = mapped_column(String)
    brought_units: Mapped[int] = mapped_column(Integer, default=0)
    sold_units: Mapped[int] = mapped_column(Integer, default=0)
    sell_through_percent: Mapped[float] = mapped_column(Float, default=0.0)


class PackagingPlan(Base):
    __tablename__ = "packaging_plans"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    bag_count: Mapped[int] = mapped_column(Integer, default=0)
    box_count: Mapped[int] = mapped_column(Integer, default=0)
    label_count: Mapped[int] = mapped_column(Integer, default=0)
    sticker_count: Mapped[int] = mapped_column(Integer, default=0)
