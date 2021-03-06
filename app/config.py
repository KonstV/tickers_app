from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    db_url: str


@lru_cache()
def get_settings() -> Settings:
    return Settings()
