from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.session import Base


class ProductionTemplate(Base):
    __tablename__ = "production_templates"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_default: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    stages = relationship(
        "ProductionTemplateStage",
        back_populates="template",
        cascade="all, delete-orphan",
    )


class ProductionTemplateStage(Base):
    __tablename__ = "production_template_stages"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    template_id: Mapped[int] = mapped_column(ForeignKey("production_templates.id"), nullable=False)

    stage_order: Mapped[int] = mapped_column(Integer)
    stage_name: Mapped[str] = mapped_column(String)

    suggested_duration_min: Mapped[int | None] = mapped_column(Integer, nullable=True)
    suggested_duration_max: Mapped[int | None] = mapped_column(Integer, nullable=True)
    alert_after_minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)

    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    template = relationship("ProductionTemplate", back_populates="stages")


class ProductionRun(Base):
    __tablename__ = "production_runs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    production_date: Mapped[str] = mapped_column(String, index=True)
    status: Mapped[str] = mapped_column(String, default="planned")
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    items = relationship(
        "ProductionItem",
        back_populates="production_run",
        cascade="all, delete-orphan",
    )


class ProductionItem(Base):
    __tablename__ = "production_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    production_run_id: Mapped[int] = mapped_column(ForeignKey("production_runs.id"), nullable=False)
    recipe_id: Mapped[int | None] = mapped_column(ForeignKey("recipes.id"), nullable=True)
    product_id: Mapped[int | None] = mapped_column(ForeignKey("products.id"), nullable=True)
    template_id: Mapped[int | None] = mapped_column(ForeignKey("production_templates.id"), nullable=True)

    source_type: Mapped[str] = mapped_column(String, default="manual")
    output_type: Mapped[str] = mapped_column(String, default="make_to_order")

    planned_quantity: Mapped[float] = mapped_column(Float, default=1.0)
    production_quantity: Mapped[float] = mapped_column(Float, default=1.0)
    good_quantity: Mapped[float] = mapped_column(Float, default=0.0)
    waste_quantity: Mapped[float] = mapped_column(Float, default=0.0)
    waste_reason: Mapped[str | None] = mapped_column(String, nullable=True)

    current_stage_index: Mapped[int] = mapped_column(Integer, default=0)
    stage_started_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    suggested_stage_end: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    status: Mapped[str] = mapped_column(String, default="planned")
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    production_run = relationship("ProductionRun", back_populates="items")
    recipe = relationship("Recipe")
    product = relationship("Product")
    template = relationship("ProductionTemplate")


class ProductionItemOrder(Base):
    __tablename__ = "production_item_orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    production_item_id: Mapped[int] = mapped_column(ForeignKey("production_items.id"), nullable=False)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False)
    quantity: Mapped[float] = mapped_column(Float, default=1.0)
