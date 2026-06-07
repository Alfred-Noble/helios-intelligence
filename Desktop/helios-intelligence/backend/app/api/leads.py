# backend/app/api/leads.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.lead import LeadCreate
from app.services.lead_service import LeadService

router = APIRouter(
    prefix="/leads",
    tags=["Leads"]
)


@router.post("/")
def create_lead(
    lead_data: LeadCreate,
    db: Session = Depends(get_db)
):
    return LeadService.create_lead(
        db=db,
        lead_data=lead_data
    )

@router.get("/")
def get_leads(
    page: int = 1,
    limit: int = 20,
    search: str | None = None,
    industry: str | None = None,
    location: str | None = None,
    db: Session = Depends(get_db)
):
    return LeadService.get_filtered_leads(
        db=db,
        page=page,
        limit=limit,
        search=search,
        industry=industry,
        location=location
    )