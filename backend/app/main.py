from fastapi import FastAPI

app = FastAPI(
    title="Stocker Pro API",
    description="Sistema de gestion de inventarios",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "mensaje": "Bienvenido a Stocker Pro"
    }