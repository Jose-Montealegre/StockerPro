from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Stocker Pro API"
    APP_DESCRIPTION: str = "Sistema de gestión de inventarios"
    APP_VERSION: str = "1.0.0"


settings = Settings()