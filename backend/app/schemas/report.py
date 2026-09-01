from datetime import datetime
from pydantic import BaseModel


class TopProductResponse(BaseModel):
    id: int
    nombre: str
    unidades_vendidas: int
    

class RecentSaleResponse(BaseModel):
    id: int
    total: float
    fecha: datetime
    

class SalesReportResponse(BaseModel):
    total_vendido: float
    numero_ventas: int 
    unidades_vendidas: int
    producto_mas_vendido: TopProductResponse | None 
    ventas_recientes: list[RecentSaleResponse]