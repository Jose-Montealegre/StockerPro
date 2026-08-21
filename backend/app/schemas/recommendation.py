from pydantic import BaseModel, ConfigDict


class RecommendationResponse(BaseModel):
    producto_id: int
    producto: str
    stock_actual: int
    estado: str 
    salidas_ultimos_7_dias: int
    rotacion: str
    recomendacion: str
    
    model_config = ConfigDict(from_attributes=True)
    