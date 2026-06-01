def simulate_capacity(projected_units: int, max_units: int):
    utilization = projected_units / max_units if max_units else 0

    overload = utilization > 0.95

    recommendation = (
        "Reduce production or reschedule."
        if overload
        else "Capacity is healthy."
    )

    return {
        "projected_utilization": utilization,
        "overload": overload,
        "recommendation": recommendation,
    }
