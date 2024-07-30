from sqlalchemy.orm import Session
from crud.favorite_crud import create_favorite, delete_favorite, update_favorite, get_favorites
from dto.favorite_dto import FavoriteCreate, FavoriteUpdate

def add_favorite(db: Session, favorite: FavoriteCreate):
    return create_favorite(db, favorite)

def remove_favorite(db: Session, favorite_id: int):
    return delete_favorite(db, favorite_id)

def modify_favorite(db: Session, favorite_id: int, favorite: FavoriteUpdate):
    return update_favorite(db, favorite_id, favorite.hospital_id)

def list_favorites(db: Session, user_id: int):
    return get_favorites(db, user_id)
