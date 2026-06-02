from app.schemas.recurring import (
    RecurringWorkflowRequest,
    RecurringWorkflowResponse,
)


def create_recurring_workflow(
    payload: RecurringWorkflowRequest,
):
    return RecurringWorkflowResponse(
        workflow_type=payload.workflow_type,
        name=payload.name,
        frequency=payload.frequency,
        target_day=payload.target_day,
        active=True,
    )
