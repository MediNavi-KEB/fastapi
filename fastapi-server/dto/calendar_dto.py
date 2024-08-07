from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CalendarCreateModel(BaseModel):
    user_id: str
    date_time: Optional[datetime]
    memo_category: Optional[str]
    memo_content: Optional[str]


class CalendarUpdateModel(BaseModel):
    calendar_id: int
    date_time: Optional[datetime] = None
    memo_category: Optional[str] = None
    memo_content: Optional[str] = None
