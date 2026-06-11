from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.schemas.project import ProjectCreate

from app.services.project_service import ProjectService

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post("/")
def create_project(
    project_data: ProjectCreate,
    db: Session = Depends(get_db)
):
    return ProjectService.create_project(
        db,
        project_data
    )


@router.get("/")
def get_projects(
    db: Session = Depends(get_db)
):
    return ProjectService.get_projects(
        db
    )

@router.post("/{project_id}/rank-leads")
def rank_leads(
    project_id: int,
    db: Session = Depends(get_db)
):
    return ProjectService.rank_leads_for_project(
        db=db,
        project_id=project_id
    )

@router.get("/{project_id}/dashboard")
def project_dashboard(
    project_id: int,
    db: Session = Depends(get_db)
):
    return ProjectService.get_project_dashboard(
        db=db,
        project_id=project_id
    )

@router.post("/{project_id}/leads/{lead_id}/generate-message")
def generate_project_message(
    project_id: int,
    lead_id: int,
    db: Session = Depends(get_db)
):
    return ProjectService.generate_project_outreach(
        db=db,
        project_id=project_id,
        lead_id=lead_id
    )