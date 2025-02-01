from pydantic_settings import SettingsConfigDict, BaseSettings
from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from typing import Annotated

class Settings(BaseSettings):
    DB_NAME_sqlite: str

    @property
    def DATABASE_URL_sqlite(self):
        return f"sqlite:///{self.DB_NAME_sqlite}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
engine = create_engine(settings.DATABASE_URL_sqlite)
session_factory = sessionmaker(engine)

str_255 = Annotated[str, 255]

class Base(DeclarativeBase):
    type_annotation_map = {
        str_255: String(255)
    }