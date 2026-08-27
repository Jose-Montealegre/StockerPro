from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.dashboard import DashboardSummaryResponse
from app.services.dashboard_service import get_dashboard_summary


router = APIRouter()


@router.get(
    "/dashboard/summary",
    response_model=DashboardSummaryResponse,
    summary="Obtener resumen del inventario",
    description="Obtiene las principales métricas del inventario."
)
def get_dashboard_summary_route(
    db: Session = Depends(get_db)
):
    return get_dashboard_summary(db)