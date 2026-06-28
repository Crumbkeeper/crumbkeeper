from pydantic import BaseModel


class ProductionRunBase(BaseModel):
    name: str
    production_date: str
    status: str = "planned"
    notes: str | None = None


class ProductionRunCreate(ProductionRunBase):
    pass


class ProductionRunUpdate(ProductionRunBase):
    pass


class ProductionRunResponse(ProductionRunBase):
    id: int

    class Config:
        from_attributes = True


class ProductionRunComplete(BaseModel):
    notes: str | None = None


class ProductionItemBase(BaseModel):
    production_run_id: int
    recipe_id: int | None = None
    product_id: int | None = None
    template_id: int | None = None

    source_type: str = "manual"
    output_type: str = "make_to_order"

    planned_quantity: float = 1.0
    production_quantity: float = 1.0
    good_quantity: float = 0.0
    waste_quantity: float = 0.0
    waste_reason: str | None = None

    current_stage_index: int = 0
    status: str = "planned"
    notes: str | None = None


class ProductionItemCreate(ProductionItemBase):
    pass


class ProductionItemUpdate(ProductionItemBase):
    pass


class ProductionItemResponse(ProductionItemBase):
    id: int

    class Config:
        from_attributes = True


class ProductionItemAdvanceStage(BaseModel):
    delay_minutes: int | None = None


class ProductionItemComplete(BaseModel):
    good_quantity: float
    waste_quantity: float = 0.0
    waste_reason: str | None = None
    notes: str | None = None
