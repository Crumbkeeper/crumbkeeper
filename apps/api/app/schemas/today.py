from pydantic import BaseModel


class TodaySimulationRequest(BaseModel):
    pending_tasks: int
    urgent_tasks: int


class TodaySimulationResponse(BaseModel):
    operational_load: float
    alert_triggered: bool
    recommendation: str
