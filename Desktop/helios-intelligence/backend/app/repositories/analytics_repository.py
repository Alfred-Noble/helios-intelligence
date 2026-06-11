from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.lead import Lead


class AnalyticsRepository:

    @staticmethod
    def get_summary(db: Session):

        total_leads = db.query(Lead).count()

        high_potential = (
            db.query(Lead)
            .filter(Lead.ai_score >= 70)
            .count()
        )

        medium_potential = (
            db.query(Lead)
            .filter(
                Lead.ai_score >= 40,
                Lead.ai_score < 70
            )
            .count()
        )

        low_potential = (
            db.query(Lead)
            .filter(Lead.ai_score < 40)
            .count()
        )

        top_location = (
            db.query(
                Lead.location,
                func.count(Lead.id)
            )
            .group_by(Lead.location)
            .order_by(func.count(Lead.id).desc())
            .first()
        )

        top_industry = (
            db.query(
                Lead.industry,
                func.count(Lead.id)
            )
            .group_by(Lead.industry)
            .order_by(func.count(Lead.id).desc())
            .first()
        )

        return {
            "total_leads": total_leads,
            "high_potential": high_potential,
            "medium_potential": medium_potential,
            "low_potential": low_potential,
            "top_location": top_location[0] if top_location else None,
            "top_industry": top_industry[0] if top_industry else None
        }