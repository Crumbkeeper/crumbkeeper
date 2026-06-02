from fastapi import APIRouter

from app.schemas.automation import (
    AutomationRequest,
    AutomationResponse,
)
from app.services.automation_engine import (
    run_automation,
)

router = APIRouter()


@router.post(
    "/automation/run",
    response_model=AutomationResponse,
)
def run(
    payload: AutomationRequest,
):
    return run_automation(
        payload.inventory_risk,
        payload.projected_utilization,
        payload.upcoming_market,
    )
