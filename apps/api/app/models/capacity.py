from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.session import Base


class BakeryCapacityProfile(Base):
    __tablename__ = "bakery_capacity_profiles"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    name: Mapped[str] = mapped_column(String, default="Default Capacity")
    overload_threshold: Mapped[float] = mapped_column(Float, default=0.95)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class CategoryCapacity(Base):
    __tablename__ = "category_capacities"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    category: Mapped[str] = mapped_column(String)
    max_units: Mapped[int] = mapped_column(default=0)
    labor_hours: Mapped[float] = mapped_column(Float, default=0)


class TimeBlockAvailability(Base):
    __tablename__ = "time_block_availability"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    day_of_week: Mapped[str] = mapped_column(String)
    start_time: Mapped[str] = mapped_column(String)
    end_time: Mapped[str] = mapped_column(String)


class EquipmentConstraint(Base):
    __tablename__ = "equipment_constraints"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    equipment_type: Mapped[str] = mapped_column(String)
    capacity: Mapped[int] = mapped_column(default=0)


class CapacitySnapshot(Base):
    __tablename__ = "capacity_snapshots"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    utilization_percent: Mapped[float] = mapped_column(Float, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
