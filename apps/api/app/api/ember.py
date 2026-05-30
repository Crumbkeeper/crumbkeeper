from fastapi import APIRouter

from app.services.ember import ember_service


router = APIRouter(
    prefix="/ember",
    tags=["ember"],
)


@router.get("/guidance")
def get_guidance():
    return ember_service.get_daily_guidance()


@router.get("/analyze")
def analyze():
    return ember_service.analyze_production()