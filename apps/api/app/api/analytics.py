from fastapi import APIRouter

from app.schemas.analytics import AnalyticsSimulationRequest
from app.schemas.analytics import AnalyticsSimulationResponse
from app.services.analytics_engine import simulate_analytics

router = APIRouter()


@router.post("/analytics/simulate", response_model=AnalyticsSimulationResponse)
def simulate(payload: AnalyticsSimulationRequest):
    return simulate_analytics(
        payload.completed_tasks,
        payload.delayed_tasks,
        payload.total_capacity,
        payload.used_capacity,
        payload.revenue,
        payload.labor_hours,
    )


@router.get("/analytics")
def get_analytics_overview():
    return {
        "module": "operational analytics",
        "status": "operational",
        "metrics": [
            "production efficiency",
            "capacity utilization",
            "revenue per labor hour",
            "workload risk",
        ],
    }
