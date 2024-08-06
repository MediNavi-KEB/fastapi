from sqlalchemy import Column, String, Integer, ForeignKey
from db.session import Base

class Favorite(Base):
    __tablename__ = "favorites"

    favorite_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50), ForeignKey('users.user_id'), index=True)
    hospital_name = Column(String(255), nullable=False)
