from sqlalchemy.orm import Session
from fastapi import HTTPException
from crud.news_crud import get_news as crud_get_news
from crawler.news_crawler import crawl_and_store


def get_news(db: Session, user_id: str):
    news = crud_get_news(db, user_id)
    if news is None:
        raise HTTPException(status_code=404, detail="해당 유저에 적합한 뉴스를 찾을 수 없습니다.")
    return news


def start_crawl_and_store(db: Session, user_id: str, disease_name: str):
    if not user_id or not disease_name:
        raise HTTPException(status_code=400, detail="user_id and disease_name are required")
    crawl_and_store(db, user_id, disease_name)
    return {"message": "Crawling started"}
