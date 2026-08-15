from pydantic import BaseModel


class MovementCreate(BaseModel):
    product_id: int
    tipo: str
    cantidad: int


class MovementResponse(BaseModel):
    id: int
    product_id: int
    tipo: str
    cantidad: int