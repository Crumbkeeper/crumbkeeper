from pydantic import BaseModel


class ProductionRunCreate(BaseModel):
    name: str
    status: str = "planned"


class ProductionRunResponse(BaseModel):
    id: int
    name: str
    status: str

    class Config:
        from_attributes = True
