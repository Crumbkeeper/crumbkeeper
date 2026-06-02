from fastapi import APIRouter

from app.schemas.forecast import (
    InventoryProjectionSimulationRequest,
    InventoryProjectionSimulationResponse,
)
from app.services.inventory_projection_engine import (
    simulate_inventory_projection,
)

router = APIRouter()


@router.post(
    "/inventory-projections/simulate",
    response_model=InventoryProjectionSimulationResponse,
)
def simulate(
    payload: InventoryProjectionSimulationRequest,
):
    return simulate_inventory_projection(
        payload.current_stock,
        payload.projected_usage,
    )
