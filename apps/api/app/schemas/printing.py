from pydantic import BaseModel


class PrintRequest(BaseModel):
    document_type: str
    bakery_name: str


class PrintResponse(BaseModel):
    document_type: str
    generated: bool
    content: str
