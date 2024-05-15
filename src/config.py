import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict()

    PROJECT_NAME: str = "Pluto API"
    API_V1_STR: str = "/api/v1"

    ALLOWED_ORIGINS: list[str] = ["http://localhost:8000"]

    DATABASE_URL: str = str(os.getenv("POSTGRES_URL"))


settings = Settings()
