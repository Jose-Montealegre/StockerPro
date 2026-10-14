
import os

from dotenv import load_dotenv
from google import genai

from app.services.recommendation_service import get_recommendations


load_dotenv()


def get_ai_recommendation_data(db):
    recommendations = get_recommendations(db)

    return {
        "total_productos_analizados": len(recommendations),
        "recomendaciones": recommendations
    }


def test_gemini_connection():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("No se encontró GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=(
            "Responde únicamente con una frase corta "
            "confirmando que la inteligencia artificial "
            "de Stocker Pro está funcionando."
        )
    )

    return response.text


def generate_ai_recommendations(db):
    data = get_ai_recommendation_data(db)

    if not data["recomendaciones"]:
        return "Actualmente no hay productos que requieran recomendaciones."

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("No se encontró GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    prompt = f"""
    Eres un asistente de inventarios de Stocker Pro,
    un sistema de gestión de inventarios para pequeñas empresas.

    Analiza las siguientes recomendaciones:
    {data["recomendaciones"]}

    Genera una explicación breve en español para cada producto.

    Reglas:
    - Utiliza únicamente los datos proporcionados.
    - No inventes cantidades, ventas ni fechas.
    - No modifiques la cantidad sugerida de reposición.
    - Explica el estado del stock y la rotación.
    - Presenta recomendaciones claras y profesionales.
    - Si la reposición sugerida es 0, explica que
      el cálculo actual no requiere unidades adicionales.
    - No afirmes que habrá ventas futuras garantizadas.
    """

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    return response.text
