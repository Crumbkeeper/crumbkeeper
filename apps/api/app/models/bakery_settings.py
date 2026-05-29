from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.session import Base


class BakerySettings(Base):
    __tablename__ = "bakery_settings"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    bakery_id: Mapped[int] = mapped_column(
        ForeignKey("bakeries.id"),
        unique=True,
        nullable=False,
    )

    timezone: Mapped[str] = mapped_column(
        String,
        default="America/New_York",
    )

    default_fermentation_temp: Mapped[float] = mapped_column(
        Float,
        default=72.0,
    )

    default_lead_time_days: Mapped[int] = mapped_column(
        Integer,
        default=3,
    )

    preferred_unit: Mapped[str] = mapped_column(
        String,
        default="g",
    )

    bakery = relationship("Bakery", back_populates="settings")
