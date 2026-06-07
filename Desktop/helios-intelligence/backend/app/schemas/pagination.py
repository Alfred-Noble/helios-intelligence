from pydantic import BaseModel
from typing import Any


class PaginatedResponse(BaseModel):
    items: list[Any]
    page: int
    limit: int
    total: int
    total_pages: int