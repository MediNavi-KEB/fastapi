from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class CalendarCreateModel(BaseModel):
    user_id: str
    start_date: datetime
    end_date: datetime
    memo_category: Optional[str]
    memo_content: Optional[str]


class CalendarUpdateModel(BaseModel):
    date_time: Optional[datetime] = None
    memo_category: Optional[str] = None
    memo_content: Optional[str] = None


class CalendarReadModel(BaseModel):
    calendar_id: int
    user_id: str
    date_time: Optional[datetime]
    memo_category: str
    memo_content: str
