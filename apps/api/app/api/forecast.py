from fastapi import APIRouter

from app.schemas.forecast import ForecastSimulationRequest
from app.services.forecast_engine import simulate_forecast

router = APIRouter()


@router.post("/forecast/simulate")
def simulate(payload: ForecastSimulationRequest):
    return simulate_forecast(
        payload.current_orders,
        payload.historical_average,
        payload.growth_target,
    )
