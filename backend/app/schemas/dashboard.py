from pydantic import BaseModel


class DashboardSummaryResponse(BaseModel):
    total_productos: int 
    total_unidades: int
    productos_stock_bajo: int
    productos_agotados: int
    total_categorias: int
        