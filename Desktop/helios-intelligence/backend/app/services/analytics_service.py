from sqlalchemy.orm import Session

from app.repositories.analytics_repository import AnalyticsRepository


class AnalyticsService:

    @staticmethod
    def get_summary(
        db: Session
    ):
        return AnalyticsRepository.get_summary(
            db=db
        )