from pydantic import BaseModel


class ForecastSimulationRequest(BaseModel):
    current_orders: int
    historical_average: int
    growth_target: int


class ForecastSimulationResponse(BaseModel):
    projected_demand: float
    shortage_risk: bool
    recommendation: str
