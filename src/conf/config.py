from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    sqlalchemy_database_url: str
    secret_key: str
    algorithm: str


settings = Settings()