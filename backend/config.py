from pydantic import Field, model_validator
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    TOKEN_SECRET_KEY: str
    TOKEN_ALGORITHM: str
    TOKEN_EXPIRATION_MINUTES: int
    sqlalchemy_url: str | None = Field(default=None, validation_alias="sqlalchemy.url")
    @model_validator(mode="after")
    def assemble_sqlalchemy_url(self):
        if self.sqlalchemy_url is None:
            user = self.POSTGRES_USER
            password = self.POSTGRES_PASSWORD
            db = self.POSTGRES_DB
            host = self.POSTGRES_HOST
            port = self.POSTGRES_PORT
            self.sqlalchemy_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
        return self