# backend/app/api/leads.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import UploadFile, File
from app.utils.csv_parser import read_csv
from app.utils.csv_parser import (
    read_csv,
    convert_rows_to_leads
)

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

@router.post("/upload-csv")
def upload_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if not file.filename.endswith(".csv"):
        return {
            "error": "Only CSV files are allowed"
        }

    df = read_csv(file.file)

    leads = convert_rows_to_leads(df)

    return LeadService.import_csv(
        db=db,
        leads=leads
    )

@router.post("/{lead_id}/score")
def score_lead(
    lead_id: int,
    db: Session = Depends(get_db)
):
    return LeadService.score_lead(
        db=db,
        lead_id=lead_id
    )

@router.post("/{lead_id}/generate-message")
def generate_message(
    lead_id: int,
    db: Session = Depends(get_db)
):
    return LeadService.generate_message(
        db=db,
        lead_id=lead_id
    )