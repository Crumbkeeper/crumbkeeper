from fastapi import APIRouter

from app.schemas.today import TodaySimulationRequest
from app.services.today_engine import simulate_today

router = APIRouter()


@router.post("/today/simulate")
def simulate(payload: TodaySimulationRequest):
    return simulate_today(
        payload.pending_tasks,
        payload.urgent_tasks,
    )
