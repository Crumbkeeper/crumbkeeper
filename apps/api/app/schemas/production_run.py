from pydantic import BaseModel


class ProductionRunBase(BaseModel):
    task_name: str
    scheduled_time: str
    linked_order_id: int | None = None
    status: str = "scheduled"


class ProductionRunCreate(ProductionRunBase):
    pass


class ProductionRunUpdate(ProductionRunBase):
    pass


class ProductionRunResponse(ProductionRunBase):
    id: int

    class Config:
        from_attributes = True