# main.py
from apis.base import _api_router
from core.config import settings
from db.base import Base
from db.session import engine
from fastapi import FastAPI


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(_api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app


app = start_application()


@app.get("/")
def hello_api():
    return {"msg": "Hello FastAPI🚀"}
