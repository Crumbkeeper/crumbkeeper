from pydantic import BaseModel


class ProductionTemplateBase(BaseModel):
    name: str
    description: str | None = None
    is_default: bool = False


class ProductionTemplateCreate(ProductionTemplateBase):
    pass


class ProductionTemplateUpdate(ProductionTemplateBase):
    pass


class ProductionTemplateResponse(ProductionTemplateBase):
    id: int

    class Config:
        from_attributes = True


class ProductionTemplateStageBase(BaseModel):
    stage_order: int
    stage_name: str

    suggested_duration_min: int | None = None
    suggested_duration_max: int | None = None

    alert_after_minutes: int | None = None

    notes: str | None = None


class ProductionTemplateStageCreate(ProductionTemplateStageBase):
    pass


class ProductionTemplateStageResponse(ProductionTemplateStageBase):
    id: int
    template_id: int

    class Config:
        from_attributes = True
