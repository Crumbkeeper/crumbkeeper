from pydantic import BaseModel


class ProductionRunBase(BaseModel):
    task_name: str
    scheduled_time: str
    linked_order_id: int | None = None

    stage: str = "prep"
    priority: str = "normal"
    batch_size: int = 1
    dough_weight: float = 0.0
    notes: str | None = None

    status: str = "scheduled"


class ProductionRunCreate(ProductionRunBase):
    pass


class ProductionRunUpdate(ProductionRunBase):
    pass


class ProductionRunResponse(ProductionRunBase):
    id: int

    class Config:
        from_attributes = True
