from fastapi import APIRouter

from app.schemas.recurring import (
    RecurringWorkflowRequest,
    RecurringWorkflowResponse,
)
from app.services.recurring_engine import (
    create_recurring_workflow,
)

router = APIRouter()


@router.post(
    "/recurring-workflows",
    response_model=RecurringWorkflowResponse,
)
def create_workflow(
    payload: RecurringWorkflowRequest,
):
    return create_recurring_workflow(payload)
