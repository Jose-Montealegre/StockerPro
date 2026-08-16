from enum import Enum
from pydantic import BaseModel,ConfigDict, Field

class MovementType(str, Enum):
    ENTRADA = "ENTRADA"
    SALIDA = "SALIDA"
class MovementCreate(BaseModel):
    product_id: int
    tipo: MovementType
    cantidad: int = Field(gt=0)


class MovementResponse(BaseModel):
    id: int
    product_id: int
    tipo: MovementType
    cantidad: int
    
model_config = ConfigDict(from_attributes=True)