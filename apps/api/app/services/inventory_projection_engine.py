from app.schemas.forecast import InventoryProjectionSimulationRequest
from app.schemas.forecast import InventoryProjectionSimulationResponse


def simulate_inventory_projection(
    current_stock: float,
    projected_usage: float,
):
    projected_remaining = current_stock - projected_usage

    if projected_remaining <= 0:
        risk_level = "critical"
        restock_required = True
    elif projected_remaining <= current_stock * 0.25:
        risk_level = "low"
        restock_required = True
    else:
        risk_level = "healthy"
        restock_required = False

    return InventoryProjectionSimulationResponse(
        projected_remaining=projected_remaining,
        risk_level=risk_level,
        restock_required=restock_required,
    )
