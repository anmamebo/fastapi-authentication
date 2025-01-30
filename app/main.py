from contextlib import asynccontextmanager

from app.database.connection import create_db_and_tables
from app.routes import auth
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Inicialization of the database and tables."""
    create_db_and_tables()  # Ejecuta antes de que la app arranque
    yield  # Aquí FastAPI ejecuta la aplicación normalmente


app = FastAPI(lifespan=lifespan)


app.include_router(auth.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
