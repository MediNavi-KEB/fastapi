from sqlalchemy.orm import Session
from crud.favorite_crud import get_favorite, create_favorite, get_favorites, update_favorite, delete_favorite
from dto.favorite_dto import FavoriteCreate, FavoriteUpdate, Favorite


def get_favorite_service(db: Session, favorite_id: int):
    return get_favorite(db, favorite_id)


def create_favorite_service(db: Session, favorite: FavoriteCreate):
    favorite_model = Favorite(name=favorite.name, user_id=favorite.user_id)
    return create_favorite(db, favorite_model)


def get_favorites_service(db: Session, skip: int = 0, limit: int = 10):
    return get_favorites(db, skip, limit)


def update_favorite_service(db: Session, favorite_id: int, favorite: FavoriteUpdate):
    return update_favorite(db, favorite_id, favorite.name, favorite.user_id)


def delete_favorite_service(db: Session, favorite_id: int):
    return delete_favorite(db, favorite_id)
