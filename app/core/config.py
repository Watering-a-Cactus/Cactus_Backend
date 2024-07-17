from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GPT_API_KEY: str
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()