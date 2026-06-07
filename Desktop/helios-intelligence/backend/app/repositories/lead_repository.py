from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.lead import Lead
from app.schemas.lead import LeadCreate


class LeadRepository:

    @staticmethod
    def create(db: Session, lead_data: LeadCreate):
        lead = Lead(**lead_data.model_dump())

        db.add(lead)
        db.commit()
        db.refresh(lead)

        return lead
       
    @staticmethod
    def get_filtered_leads(
        db: Session,
        page: int = 1,
        limit: int = 20,
        search: str | None = None,
        industry: str | None = None,
        location: str | None = None
    ):
        offset = (page - 1) * limit

        query = db.query(Lead)

        if search:
            query = query.filter(
                or_(
                    Lead.full_name.ilike(f"%{search}%"),
                    Lead.company.ilike(f"%{search}%"),
                    Lead.headline.ilike(f"%{search}%"),
                    Lead.industry.ilike(f"%{search}%"),
                    Lead.location.ilike(f"%{search}%")
                )
            )

        if industry:
            query = query.filter(
                Lead.industry.ilike(f"%{industry}%")
            )

        if location:
            query = query.filter(
                Lead.location.ilike(f"%{location}%")
            )

        total = query.count()

        items = (
            query
            .offset(offset)
            .limit(limit)
            .all()
        )

        return items, total
    
