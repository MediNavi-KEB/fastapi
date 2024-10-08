from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from services.news_service import get_news, start_crawl_and_store
from db.connection import get_db
from dto.news_dto import NewsCreateModel, NewsCrawlerModel
import logging
from db.models.news import Base
from db.session import engine
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

news_router = APIRouter(tags=["News"])


@news_router.get("/read/{user_id}", response_model=List[NewsCreateModel])
def read_news(user_id: str, db: Session = Depends(get_db)):
    return get_news(db, user_id)


@news_router.on_event("startup")
def on_startup():
    logger.info("Starting up and creating database tables if not exist")
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        logger.error(f"Error during table creation: {e}")


@news_router.post("/crawler")
async def login_and_crawl(request: NewsCrawlerModel, db: Session = Depends(get_db)):
    return start_crawl_and_store(db, request.user_id, request.disease_name)
