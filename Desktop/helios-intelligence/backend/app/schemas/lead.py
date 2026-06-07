from pydantic import BaseModel
from typing import Optional


class LeadCreate(BaseModel):
    full_name: str
    headline: Optional[str] = None
    company: Optional[str] = None
    industry: Optional[str] = None
    location: Optional[str] = None
    linkedin_url: Optional[str] = None
    email: Optional[str] = None
    bio: Optional[str] = None


class LeadUpdate(BaseModel):
    headline: Optional[str] = None
    company: Optional[str] = None
    industry: Optional[str] = None
    location: Optional[str] = None
    linkedin_url: Optional[str] = None
    email: Optional[str] = None
    bio: Optional[str] = None
    ai_score: Optional[int] = None
    ai_reason: Optional[str] = None
    outreach_message: Optional[str] = None
    status: Optional[str] = None


class LeadResponse(BaseModel):
    id: int
    full_name: str

    class Config:
        from_attributes = True