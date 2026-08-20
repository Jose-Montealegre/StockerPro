from enum import Enum
from pydantic import BaseModel, ConfigDict, Field


class MovementType(str, Enum):
    ENTRADA = "ENTRADA"
    SALIDA = "SALIDA"


class MovementCreate(BaseModel):
    product_id: int
    tipo: MovementType
    cantidad: int = Field(gt=0)


class ProductMovementResponse(BaseModel):
    id: int
    nombre: str
    precio: float
    stock: int

    model_config = ConfigDict(from_attributes=True)


class MovementResponse(BaseModel):
    id: int
    tipo: MovementType
    cantidad: int
    stock_anterior: int
    stock_resultante: int
    
    
    producto: ProductMovementResponse = Field(
        validation_alias="product"
    )

    model_config = ConfigDict(from_attributes=True)