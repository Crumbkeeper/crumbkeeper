from pydantic import BaseModel


class ForecastSimulationRequest(BaseModel):
    current_orders: int
    historical_average: int
    growth_target: int


class ForecastSimulationResponse(BaseModel):
    projected_demand: float
    shortage_risk: bool
    recommendation: str


class InventoryProjectionSimulationRequest(BaseModel):
    current_stock: float
    projected_usage: float


class InventoryProjectionSimulationResponse(BaseModel):
    projected_remaining: float
    risk_level: str
    restock_required: bool
