def simulate_market(
    expected_customers: int,
    planned_units: int,
    average_sale_price: float,
    packaging_units_available: int,
):
    sell_through = expected_customers / planned_units if planned_units else 0
    sell_through_percent = min(sell_through * 100, 100)
    projected_units_sold = min(expected_customers, planned_units)
    projected_revenue = projected_units_sold * average_sale_price
    overproduction_risk = sell_through_percent < 75
    packaging_shortage = (
        packaging_units_available > 0
        and packaging_units_available < planned_units
    )

    if packaging_shortage:
        recommendation = "Increase packaging before market prep."
    elif overproduction_risk:
        recommendation = "Reduce planned units or shift excess to preorder pickup."
    else:
        recommendation = "Market plan is operationally healthy."

    return {
        "projected_sell_through_percent": round(sell_through_percent, 2),
        "projected_revenue": round(projected_revenue, 2),
        "overproduction_risk": overproduction_risk,
        "packaging_shortage": packaging_shortage,
        "recommendation": recommendation,
    }


def reconcile_market(
    brought_units: int,
    sold_units: int,
    average_sale_price: float,
):
    sell_through = sold_units / brought_units if brought_units else 0
    sell_through_percent = sell_through * 100
    revenue = sold_units * average_sale_price
    leftover_units = max(brought_units - sold_units, 0)

    if sell_through_percent >= 90:
        recommendation = "Increase next market prep slightly."
    elif sell_through_percent < 65:
        recommendation = "Reduce next market prep or adjust product mix."
    else:
        recommendation = "Market volume is balanced."

    return {
        "sell_through_percent": round(sell_through_percent, 2),
        "revenue": round(revenue, 2),
        "leftover_units": leftover_units,
        "recommendation": recommendation,
    }
