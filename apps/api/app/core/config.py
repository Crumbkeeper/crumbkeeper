from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Crumbkeeper API"
    APP_ENV: str = "development"
    API_V1_PREFIX: str = "/api/v1"

    POSTGRES_USER: str = "crumbkeeper"
    POSTGRES_PASSWORD: str = "crumbkeeper"
    POSTGRES_DB: str = "crumbkeeper"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()