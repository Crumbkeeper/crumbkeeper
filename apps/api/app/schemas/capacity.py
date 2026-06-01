from pydantic import BaseModel


class CapacityProfileResponse(BaseModel):
    bakery_id: int
    name: str
    overload_threshold: float

    class Config:
        from_attributes = True


class CapacitySimulationRequest(BaseModel):
    projected_units: int
    category: str


class CapacitySimulationResponse(BaseModel):
    projected_utilization: float
    overload: bool
    recommendation: str
