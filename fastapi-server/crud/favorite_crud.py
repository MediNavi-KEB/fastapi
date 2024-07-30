from sqlalchemy.orm import Session
from db.models.favorite import Favorite
from dto.favorite_dto import FavoriteCreate

def create_favorite(db: Session, favorite: FavoriteCreate):
    db_favorite = Favorite(user_id=favorite.user_id, hospital_id=favorite.hospital_id)
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    return db_favorite

def delete_favorite(db: Session, favorite_id: int):
    db_favorite = db.query(Favorite).filter(Favorite.id == favorite_id).first()
    if db_favorite:
        db.delete(db_favorite)
        db.commit()
        return True
    return False

def update_favorite(db: Session, favorite_id: int, hospital_id: int):
    db_favorite = db.query(Favorite).filter(Favorite.id == favorite_id).first()
    if db_favorite:
        db_favorite.hospital_id = hospital_id
        db.commit()
        db.refresh(db_favorite)
        return db_favorite
    return None

def get_favorites(db: Session, user_id: int):
    return db.query(Favorite).filter(Favorite.user_id == user_id).all()
