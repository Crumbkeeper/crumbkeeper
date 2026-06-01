from datetime import datetime
from datetime import timedelta

from fastapi import APIRouter


router = APIRouter()


@router.post("/schedule/plan")
def generate_schedule(
    due_date: str,
):
    target = datetime.fromisoformat(due_date)

    return {
        "feed_starter": (target - timedelta(hours=36)).isoformat(),
        "mix_dough": (target - timedelta(hours=24)).isoformat(),
        "bulk_fermentation": (target - timedelta(hours=18)).isoformat(),
        "shape": (target - timedelta(hours=12)).isoformat(),
        "cold_retard": (target - timedelta(hours=10)).isoformat(),
        "bake": (target - timedelta(hours=2)).isoformat(),
        "ready": target.isoformat(),
    }
