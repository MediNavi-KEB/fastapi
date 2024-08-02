from sqlalchemy import Column, String, Enum
from sqlalchemy.dialects.mysql import ENUM
from db.session import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(String(50), primary_key=True, index=True)
    password = Column(String(255), nullable=False)
    name = Column(String(100), nullable=False)
    phone = Column(String(20))
    email = Column(String(100))
    address = Column(String(255))
    gender = Column(ENUM('남성', '여성'))