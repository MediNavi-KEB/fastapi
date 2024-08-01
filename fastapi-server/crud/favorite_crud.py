from sqlalchemy.orm import Session
from db.models.favorite import Favorite

def get_favorite(db: Session, favorite_id: int):
    return db.query(Favorite).filter(Favorite.id == favorite_id).first()

def create_favorite(db: Session, favorite: Favorite):
    db.add(favorite)
    db.commit()
    db.refresh(favorite)
    return favorite

def get_favorites(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Favorite).offset(skip).limit(limit).all()

def update_favorite(db: Session, favorite_id: int, name: str, user_id: int):
    favorite = db.query(Favorite).filter(Favorite.id == favorite_id).first()
    if favorite:
        favorite.name = name
        favorite.user_id = user_id
        db.commit()
        db.refresh(favorite)
    return favorite

def delete_favorite(db: Session, favorite_id: int):
    favorite = db.query(Favorite).filter(Favorite.id == favorite_id).first()
    if favorite:
        db.delete(favorite)
        db.commit()
    return favorite
