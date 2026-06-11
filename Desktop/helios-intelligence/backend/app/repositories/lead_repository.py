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
    
    @staticmethod
    def bulk_create(
        db: Session,
        leads: list
    ):
        db.add_all(leads)
        db.commit()

    @staticmethod
    def get_by_id(
        db: Session,
        lead_id: int
    ):
        return (
            db.query(Lead)
            .filter(Lead.id == lead_id)
            .first()
        )


    @staticmethod
    def save(
        db: Session,
        lead: Lead
    ):
        db.commit()
        db.refresh(lead)

        return lead
    
    @staticmethod
    def exists_by_email_or_linkedin(
        db: Session,
        email: str | None,
        linkedin_url: str | None
    ):
        query = db.query(Lead)

        if email:
            existing = query.filter(
                Lead.email == email
            ).first()

            if existing:
                return True

        if linkedin_url:
            existing = query.filter(
                Lead.linkedin_url == linkedin_url
            ).first()

            if existing:
                return True

        return False
    
    @staticmethod
    def get_all_leads(
        db: Session
    ):
        return db.query(Lead).all()