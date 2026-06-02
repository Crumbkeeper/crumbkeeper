from pydantic import BaseModel


class MarketSimulationRequest(BaseModel):
    expected_customers: int
    planned_units: int
    average_sale_price: float = 8.0
    packaging_units_available: int = 0


class MarketSimulationResponse(BaseModel):
    projected_sell_through_percent: float
    projected_revenue: float
    overproduction_risk: bool
    packaging_shortage: bool
    recommendation: str


class MarketReconciliationRequest(BaseModel):
    brought_units: int
    sold_units: int
    average_sale_price: float = 8.0


class MarketReconciliationResponse(BaseModel):
    sell_through_percent: float
    revenue: float
    leftover_units: int
    recommendation: str
