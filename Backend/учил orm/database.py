from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from config import settings
from typing import Annotated

engine = create_engine(settings.DATABASE_URL_sqlite)

session_factory = sessionmaker(engine)

str_255 = Annotated[str, 255]

class Base(DeclarativeBase):
    type_annotation_map = {
        str_255: String(255)
    }