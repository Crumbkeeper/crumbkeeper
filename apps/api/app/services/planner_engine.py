def simulate_plan(
    projected_units: int,
    available_hours: float,
):
    utilization = projected_units / available_hours if available_hours else 0

    conflict = utilization > 10

    recommendation = (
        "Reschedule production blocks."
        if conflict
        else "Production plan is viable."
    )

    return {
        "utilization": utilization,
        "conflict_detected": conflict,
        "recommendation": recommendation,
    }
