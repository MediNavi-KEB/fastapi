from sqlalchemy.orm import Session
from db.models.favorite import Favorite
from dto.favorite_dto import FavoriteCreateModel, FavoriteUpdateModel


def create_favorite(db: Session, favorite: FavoriteCreateModel):
    db_favorite = Favorite(
        user_id=favorite.user_id,
        hospital_name=favorite.hospital_name,
        hospital_address=favorite.hospital_address,
        hospital_phone=favorite.hospital_phone
    )
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    return db_favorite


def get_favorites_by_user_id(db: Session, user_id: str):
    return db.query(Favorite).filter(Favorite.user_id == user_id).all()


def delete_favorite_by_name(db: Session, user_id: str, hospital_name: str):
    db_favorite = db.query(Favorite).filter(Favorite.user_id == user_id, Favorite.hospital_name == hospital_name).first()
    if db_favorite:
        db.delete(db_favorite)
        db.commit()
    return db_favorite


def delete_favorite_by_id(db: Session, favorite_id: int):
    db_favorite = db.query(Favorite).filter(Favorite.favorite_id == favorite_id).first()
    if db_favorite:
        db.delete(db_favorite)
        db.commit()
    return db_favorite


def update_favorite(db: Session, favorite_id: int, favorite_update: FavoriteUpdateModel):
    db_favorite = db.query(Favorite).filter(Favorite.favorite_id == favorite_id).first()
    if db_favorite is None:
        return None
    db_favorite.hospital_name = favorite_update.hospital_name
    db_favorite.hospital_address = favorite_update.hospital_address
    db_favorite.hospital_phone = favorite_update.hospital_phone
    db.commit()
    db.refresh(db_favorite)
    return db_favorite
