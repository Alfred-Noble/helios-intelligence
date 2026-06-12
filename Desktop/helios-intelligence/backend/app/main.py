from fastapi import FastAPI

from app.db.init_db import init_db
from app.api.leads import router as lead_router
from app.api.analytics import router as analytics_router
from app.api.projects import router as project_router
from app.api.auth import router as auth_router

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

app.include_router(lead_router)
app.include_router(analytics_router)
app.include_router(project_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Helios Backend Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}