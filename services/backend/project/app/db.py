import os

from sqlmodel import create_engine, SQLModel, Session
from app.config import get_settings

settings = get_settings()
print(settings)
DATABASE_URL = os.environ.get("DATABASE_TEST_URL")
print(DATABASE_URL)
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session