from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.production_run import ProductionTemplate
from app.models.production_run import ProductionTemplateStage
from app.schemas.production_template import ProductionTemplateCreate
from app.schemas.production_template import ProductionTemplateResponse
from app.schemas.production_template import ProductionTemplateStageCreate
from app.schemas.production_template import ProductionTemplateStageResponse
from app.schemas.production_template import ProductionTemplateUpdate


router = APIRouter()


@router.post(
    "/production-templates",
    response_model=ProductionTemplateResponse,
)
def create_production_template(
    payload: ProductionTemplateCreate,
    db: Session = Depends(get_db),
):
    template = ProductionTemplate(**payload.model_dump())

    db.add(template)
    db.commit()
    db.refresh(template)

    return template


@router.get(
    "/production-templates",
    response_model=list[ProductionTemplateResponse],
)
def list_production_templates(
    db: Session = Depends(get_db),
):
    return db.query(ProductionTemplate).all()


@router.get(
    "/production-templates/{template_id}",
    response_model=ProductionTemplateResponse,
)
def get_production_template(
    template_id: int,
    db: Session = Depends(get_db),
):
    template = (
        db.query(ProductionTemplate)
        .filter(ProductionTemplate.id == template_id)
        .first()
    )

    if not template:
        raise HTTPException(
            status_code=404,
            detail="Production template not found",
        )

    return template


@router.put(
    "/production-templates/{template_id}",
    response_model=ProductionTemplateResponse,
)
def update_production_template(
    template_id: int,
    payload: ProductionTemplateUpdate,
    db: Session = Depends(get_db),
):
    template = (
        db.query(ProductionTemplate)
        .filter(ProductionTemplate.id == template_id)
        .first()
    )

    if not template:
        raise HTTPException(
            status_code=404,
            detail="Production template not found",
        )

    for key, value in payload.model_dump().items():
        setattr(template, key, value)

    db.commit()
    db.refresh(template)

    return template


@router.delete("/production-templates/{template_id}")
def delete_production_template(
    template_id: int,
    db: Session = Depends(get_db),
):
    template = (
        db.query(ProductionTemplate)
        .filter(ProductionTemplate.id == template_id)
        .first()
    )

    if not template:
        raise HTTPException(
            status_code=404,
            detail="Production template not found",
        )

    db.delete(template)
    db.commit()

    return {"message": "Production template deleted"}


@router.post(
    "/production-templates/{template_id}/stages",
    response_model=ProductionTemplateStageResponse,
)
def create_production_template_stage(
    template_id: int,
    payload: ProductionTemplateStageCreate,
    db: Session = Depends(get_db),
):
    template = (
        db.query(ProductionTemplate)
        .filter(ProductionTemplate.id == template_id)
        .first()
    )

    if not template:
        raise HTTPException(
            status_code=404,
            detail="Production template not found",
        )

    stage = ProductionTemplateStage(
        template_id=template_id,
        **payload.model_dump(),
    )

    db.add(stage)
    db.commit()
    db.refresh(stage)

    return stage


@router.get(
    "/production-templates/{template_id}/stages",
    response_model=list[ProductionTemplateStageResponse],
)
def list_production_template_stages(
    template_id: int,
    db: Session = Depends(get_db),
):
    template = (
        db.query(ProductionTemplate)
        .filter(ProductionTemplate.id == template_id)
        .first()
    )

    if not template:
        raise HTTPException(
            status_code=404,
            detail="Production template not found",
        )

    return (
        db.query(ProductionTemplateStage)
        .filter(ProductionTemplateStage.template_id == template_id)
        .order_by(ProductionTemplateStage.stage_order)
        .all()
    )


@router.put(
    "/production-template-stages/{stage_id}",
    response_model=ProductionTemplateStageResponse,
)
def update_production_template_stage(
    stage_id: int,
    payload: ProductionTemplateStageCreate,
    db: Session = Depends(get_db),
):
    stage = (
        db.query(ProductionTemplateStage)
        .filter(ProductionTemplateStage.id == stage_id)
        .first()
    )

    if not stage:
        raise HTTPException(
            status_code=404,
            detail="Production template stage not found",
        )

    for key, value in payload.model_dump().items():
        setattr(stage, key, value)

    db.commit()
    db.refresh(stage)

    return stage


@router.delete("/production-template-stages/{stage_id}")
def delete_production_template_stage(
    stage_id: int,
    db: Session = Depends(get_db),
):
    stage = (
        db.query(ProductionTemplateStage)
        .filter(ProductionTemplateStage.id == stage_id)
        .first()
    )

    if not stage:
        raise HTTPException(
            status_code=404,
            detail="Production template stage not found",
        )

    db.delete(stage)
    db.commit()

    return {"message": "Production template stage deleted"}
