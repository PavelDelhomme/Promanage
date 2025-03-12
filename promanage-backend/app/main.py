from fastapi import FastAPI
from .db.session import engine, Base
from .api.v1.endpoints import cv, blog, projects
from .admin import setup_admin

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ProManage API",
    description="API de gestion de portfolio et CV professionnel",
    version="1.0.0",
)
app.on_event("statup")(setup_admin)
app.include_router(projects.router, prefix="/api/v1")
app.include_router(cv.router, prefix="/api/v1")
app.include_router(blog.router, prefix="/api/v1")
