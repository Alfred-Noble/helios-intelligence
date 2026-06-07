from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime, timezone

from app.db.base import Base


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)
    headline = Column(String)

    company = Column(String)
    industry = Column(String)

    location = Column(String)

    linkedin_url = Column(String)
    email = Column(String)

    bio = Column(Text)

    ai_score = Column(Integer)

    ai_reason = Column(Text)

    outreach_message = Column(Text)

    email = Column(String)

    status = Column(String, default="New")

    status = Column(String, default="New")

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )