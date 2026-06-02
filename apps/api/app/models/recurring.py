from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.session import Base


class RecurringWorkflow(Base):
    __tablename__ = "recurring_workflows"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    workflow_type: Mapped[str] = mapped_column(
        String,
    )

    name: Mapped[str] = mapped_column(
        String,
    )

    frequency: Mapped[str] = mapped_column(
        String,
    )

    target_day: Mapped[str] = mapped_column(
        String,
    )

    active: Mapped[bool] = mapped_column(
        default=True,
    )
