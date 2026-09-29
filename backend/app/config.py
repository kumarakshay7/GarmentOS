from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "GarmentOS API"
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/garmentos"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
