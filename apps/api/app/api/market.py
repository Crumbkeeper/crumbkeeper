from fastapi import APIRouter

from app.schemas.market import MarketReconciliationRequest
from app.schemas.market import MarketSimulationRequest
from app.schemas.market import MarketSimulationResponse
from app.schemas.market import MarketReconciliationResponse
from app.services.market_engine import reconcile_market
from app.services.market_engine import simulate_market

router = APIRouter()


@router.post("/markets/simulate", response_model=MarketSimulationResponse)
def simulate(payload: MarketSimulationRequest):
    return simulate_market(
        payload.expected_customers,
        payload.planned_units,
        payload.average_sale_price,
        payload.packaging_units_available,
    )


@router.post("/markets/reconcile", response_model=MarketReconciliationResponse)
def reconcile(payload: MarketReconciliationRequest):
    return reconcile_market(
        payload.brought_units,
        payload.sold_units,
        payload.average_sale_price,
    )


@router.get("/markets")
def list_markets():
    return {
        "module": "markets",
        "status": "operational",
        "features": [
            "event planning",
            "inventory prep",
            "sell-through forecasting",
            "packaging workflow",
            "post-event reconciliation",
        ],
    }
