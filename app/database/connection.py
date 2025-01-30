from typing import Annotated

from app.config import settings
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine

# URL de conexión a la base de datos (SQLite en este caso)
SQLITE_DATABASE_URL = f"sqlite:///./{settings.DB_DATABASE}"

# Crear el motor de la base de datos
connect_args = {"check_same_thread": False}
engine = create_engine(SQLITE_DATABASE_URL, connect_args=connect_args)


# Crear la base de datos y las tablas
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Obtener una sesión de la base de datos
def get_session():
    with Session(engine) as session:
        yield session


# Dependencia para obtener una sesión de la base de datos
SessionDep = Annotated[Session, Depends(get_session)]
