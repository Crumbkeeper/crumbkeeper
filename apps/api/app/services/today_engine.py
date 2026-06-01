def simulate_today(
    pending_tasks: int,
    urgent_tasks: int,
):
    load = pending_tasks + (urgent_tasks * 2)

    alert = load > 20

    recommendation = (
        "Reprioritize kitchen workflow."
        if alert
        else "Kitchen flow is stable."
    )

    return {
        "operational_load": load,
        "alert_triggered": alert,
        "recommendation": recommendation,
    }
