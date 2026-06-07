from sqlalchemy.orm import Session
import math
from app.schemas.lead import LeadCreate
from app.repositories.lead_repository import LeadRepository


class LeadService:

    @staticmethod
    def create_lead(db: Session, lead_data: LeadCreate):
        return LeadRepository.create(db, lead_data)
    
    
    @staticmethod
    def get_filtered_leads(
        db: Session,
        page: int = 1,
        limit: int = 20,
        search: str | None = None,
        industry: str | None = None,
        location: str | None = None
    ):
        items, total = LeadRepository.get_filtered_leads(
            db=db,
            page=page,
            limit=limit,
            search=search,
            industry=industry,
            location=location
        )

        return {
            "items": items,
            "page": page,
            "limit": limit,
            "total": total,
            "total_pages": math.ceil(total / limit) if total > 0 else 0,
            "search": search,
            "industry": industry,
            "location": location
        }