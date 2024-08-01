from datetime import datetime
from sqlalchemy import Column, String, Integer, Enum, DateTime, Text, ForeignKey
from sqlalchemy.dialects.mysql import ENUM
from db.session import Base


class Calendar(Base):
    __tablename__ = "calendar"

    calendar_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(String(50), ForeignKey('users.user_id'), index=True)
    date_time = Column(DateTime, default=datetime.utcnow)
    memo_category = Column(ENUM('통증', '약', '병원'))
    memo_content = Column(Text)
