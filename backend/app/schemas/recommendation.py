from pydantic import BaseModel, ConfigDict


class RecommendationResponse(BaseModel):
    producto_id: int
    producto: str
    stock_actual: int
    estado: str 
    recomendacion: str
    
    model_config = ConfigDict(from_attributes=True)
    