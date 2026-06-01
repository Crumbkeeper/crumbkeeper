from fastapi import APIRouter

from app.schemas.planner import PlannerSimulationRequest
from app.services.planner_engine import simulate_plan

router = APIRouter()


@router.post("/planner/simulate")
def simulate(payload: PlannerSimulationRequest):
    return simulate_plan(
        payload.projected_units,
        payload.available_hours,
    )
