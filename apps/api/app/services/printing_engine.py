from app.schemas.printing import (
    PrintResponse,
)


def generate_document(
    document_type: str,
    bakery_name: str,
):
    content = (
        f"{document_type} generated for {bakery_name}"
    )

    return PrintResponse(
        document_type=document_type,
        generated=True,
        content=content,
    )
