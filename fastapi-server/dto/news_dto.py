from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class NewsCreateModel(BaseModel):
    title: Optional[str]
    summary: Optional[str]
    news_date_time: Optional[datetime]
    link: Optional[str]

    class Config:
        orm_mode = True


class NewsCrawlerModel(BaseModel):
    user_id: str
    disease_name: str
