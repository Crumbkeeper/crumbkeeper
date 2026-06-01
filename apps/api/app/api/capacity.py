from fastapi import APIRouter

from app.schemas.capacity import CapacitySimulationRequest
from app.services.capacity_engine import simulate_capacity

router = APIRouter()


@router.post("/capacity/simulate")
def simulate(payload: CapacitySimulationRequest):
    return simulate_capacity(
        payload.projected_units,
        100,
    )
