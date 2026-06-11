from pydantic import BaseModel
from typing import Optional


class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None
    goal: Optional[str] = None
    industry: Optional[str] = None