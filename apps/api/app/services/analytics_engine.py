def simulate_analytics(
    completed_tasks: int,
    delayed_tasks: int,
    total_capacity: int,
    used_capacity: int,
    revenue: float,
    labor_hours: float,
):
    total_tasks = completed_tasks + delayed_tasks
    production_efficiency = completed_tasks / total_tasks if total_tasks else 0
    capacity_utilization = used_capacity / total_capacity if total_capacity else 0
    revenue_per_labor_hour = revenue / labor_hours if labor_hours else 0

    workload_risk = (
        production_efficiency < 0.75
        or capacity_utilization > 0.95
    )

    if capacity_utilization > 1:
        recommendation = "Capacity exceeded. Reduce orders or split production."
    elif production_efficiency < 0.75:
        recommendation = "Operational delays detected. Review production timing."
    elif workload_risk:
        recommendation = "Workload risk is elevated."
    else:
        recommendation = "Operations are healthy."

    return {
        "production_efficiency": round(production_efficiency, 2),
        "capacity_utilization": round(capacity_utilization, 2),
        "revenue_per_labor_hour": round(revenue_per_labor_hour, 2),
        "workload_risk": workload_risk,
        "recommendation": recommendation,
    }
