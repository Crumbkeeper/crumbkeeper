def simulate_forecast(
    current_orders: int,
    historical_average: int,
    growth_target: int,
):
    projected = (
        current_orders * 0.40
        + historical_average * 0.35
        + growth_target * 0.25
    )

    shortage = projected > 100

    recommendation = (
        "Increase prep volume."
        if shortage
        else "Forecast is within normal operating range."
    )

    return {
        "projected_demand": projected,
        "shortage_risk": shortage,
        "recommendation": recommendation,
    }
