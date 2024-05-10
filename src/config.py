from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict()

    PROJECT_NAME: str = "Pluto API"
    API_V1_STR: str = "/api/v1"


settings = Settings()
