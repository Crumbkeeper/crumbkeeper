from fastapi import APIRouter

from app.schemas.printing import (
    PrintRequest,
    PrintResponse,
)
from app.services.printing_engine import (
    generate_document,
)

router = APIRouter()


@router.post(
    "/printing/generate",
    response_model=PrintResponse,
)
def generate(
    payload: PrintRequest,
):
    return generate_document(
        payload.document_type,
        payload.bakery_name,
    )
