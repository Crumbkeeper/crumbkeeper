from app.schemas.automation import (
    AutomationResponse,
)


def run_automation(
    inventory_risk: str,
    projected_utilization: float,
    upcoming_market: bool,
):
    shopping = inventory_risk == "critical"

    production = projected_utilization > 0.75

    market = upcoming_market

    recommendation = "Automation healthy."

    if shopping:
        recommendation = (
            "Generate shopping list immediately."
        )
    elif production:
        recommendation = (
            "Generate production plan."
        )
    elif market:
        recommendation = (
            "Generate market checklist."
        )

    return AutomationResponse(
        generate_shopping_list=shopping,
        generate_production_plan=production,
        generate_market_checklist=market,
        recommendation=recommendation,
    )
