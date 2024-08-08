from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
from db.session import Base


class News(Base):
    __tablename__ = "news"

    title = Column(Text)
    news_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    summary = Column(Text)
    news_date_time = Column(DateTime)
    link = Column(String(255))
    user_id = Column(String(50), ForeignKey('users.user_id'), index=True)
    disease_name = Column(String(255), ForeignKey('diseases.disease_name'), index=True)
