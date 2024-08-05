from sqlalchemy import Column, Integer, String, ForeignKey
#from sqlalchemy.orm import relationship
from db.session import Base


class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    #user = relationship("User", back_populates="favorites")
