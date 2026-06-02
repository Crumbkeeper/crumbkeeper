from pydantic import BaseModel


class AutomationRequest(BaseModel):
    inventory_risk: str
    projected_utilization: float
    upcoming_market: bool


class AutomationResponse(BaseModel):
    generate_shopping_list: bool
    generate_production_plan: bool
    generate_market_checklist: bool
    recommendation: str
