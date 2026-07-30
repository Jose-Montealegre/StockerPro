from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "Ok",
        "message": "API funcionando correctamente"
    }