from pydantic import BaseModel


class BakeryCreate(BaseModel):
    name: str
    owner_email: str
    phone: str | None = None


class BakeryResponse(BaseModel):
    id: int
    name: str
    owner_email: str
    phone: str | None = None

    class Config:
        from_attributes = True
