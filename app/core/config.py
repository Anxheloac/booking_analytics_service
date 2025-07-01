from pydantic_settings import BaseSettings
from pydantic import AnyUrl, Field


class Settings(BaseSettings):
    # Database URL, e.g. "postgresql+asyncpg://user:pass@localhost/dbname"
    DATABASE_URL: AnyUrl = Field(..., env="DATABASE_URL")

    # Example defaults (optional)
    DEBUG: bool = False
    PAGE_SIZE: int = 50

    class Config:
        env_file = ".env"  # Load from .env file automatically
        env_file_encoding = "utf-8"


# Create a singleton settings instance
settings = Settings()
