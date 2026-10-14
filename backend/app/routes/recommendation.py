from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.ai_service import generate_ai_recommendations

from app.database import get_db
from app.schemas.recommendation import RecommendationResponse
from app.services.recommendation_service import get_recommendations


router = APIRouter()


@router.get(
    "/recommendations",
    response_model=list[RecommendationResponse],
    summary="Obtener recomendaciones de inventario",
    description="Analiza el inventario y devuelve recomendaciones para productos con stock bajo."
)
def get_recommendations_route(
    db: Session = Depends(get_db)
):
    return get_recommendations(db)


@router.get("/recommendations/ai",
            summary="Obtener recomendaciones inteligentes con IA")
def get_intelligent_recommendations(
    db: Session = Depends(get_db)
):
    explanation = generate_ai_recommendations(db)

    return {
        "tipo": "RECOMENDACION_IA",
        "explicacion": explanation
    }
