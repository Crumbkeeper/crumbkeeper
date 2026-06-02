from pydantic import BaseModel


class RecurringWorkflowRequest(BaseModel):
    workflow_type: str
    name: str
    frequency: str
    target_day: str


class RecurringWorkflowResponse(BaseModel):
    workflow_type: str
    name: str
    frequency: str
    target_day: str
    active: bool
