from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.report import SalesReportResponse
from app.services.report_service import get_sales_report


router = APIRouter(
    prefix="/reports",
    tags=["Reportes"]
)

@router.get(
    "/sales",
    response_model=SalesReportResponse,
    summary="Obtener reporte de ventas"
)
def get_sales_report_route(
    db:Session = Depends(get_db)
):
    return get_sales_report(db)