from sqlalchemy.orm import Session
from db.models.news import News
from dto.news_dto import NewsCreateModel
from sqlalchemy import func


def create_news(db: Session, news: NewsCreateModel, user_id: str, disease_name: str):
    db_news = News(**news.dict(), user_id=user_id, disease_name=disease_name)
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news


def get_news(db: Session, user_id: str, limit=2):
    news = db.query(News).filter(News.user_id == user_id).limit(limit).all()
    return news


def delete_news(db: Session, user_id: str):
    db.query(News).filter(News.user_id == user_id).delete()
    db.commit()
