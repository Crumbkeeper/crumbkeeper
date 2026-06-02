from pydantic import BaseModel


class AnalyticsSimulationRequest(BaseModel):
    completed_tasks: int
    delayed_tasks: int
    total_capacity: int
    used_capacity: int
    revenue: float
    labor_hours: float


class AnalyticsSimulationResponse(BaseModel):
    production_efficiency: float
    capacity_utilization: float
    revenue_per_labor_hour: float
    workload_risk: bool
    recommendation: str
