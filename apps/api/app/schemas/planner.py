from pydantic import BaseModel


class PlannerSimulationRequest(BaseModel):
    projected_units: int
    available_hours: float


class PlannerSimulationResponse(BaseModel):
    utilization: float
    conflict_detected: bool
    recommendation: str
