from sqlalchemy.orm import Session
from fastapi import HTTPException
from crud import favorite_crud
from dto.favorite_dto import FavoriteCreateModel, FavoriteUpdateModel
from typing import List


def create_favorite(db: Session, favorite: FavoriteCreateModel):
    return favorite_crud.create_favorite(db, favorite)


def get_favorites(db: Session, user_id: str):
    favorites = favorite_crud.get_favorites_by_user_id(db, user_id)
    if not favorites:
        raise HTTPException(status_code=404, detail="즐겨찾기 항목이 없습니다.")
    return favorites


def delete_favorite(db: Session, user_id: str, hospital_name: str):
    favorite = favorite_crud.delete_favorite_by_name(db, user_id, hospital_name)
    if not favorite:
        raise HTTPException(status_code=404, detail="삭제할 즐겨찾기 항목이 없습니다.")
    return favorite


def update_favorite(db: Session, favorite_id: int, favorite_update: FavoriteUpdateModel):
    favorite = favorite_crud.update_favorite(db, favorite_id, favorite_update)
    if not favorite:
        raise HTTPException(status_code=404, detail="수정할 즐겨찾기 항목이 없습니다.")
    return favorite
