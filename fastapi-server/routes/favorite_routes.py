from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from dto.favorite_dto import FavoriteCreate, FavoriteUpdate, FavoriteRead
from services.favorite_service import add_favorite, remove_favorite, modify_favorite, list_favorites
from typing import List

router = APIRouter()

@router.post("/", response_model=FavoriteRead)
def create_favorite(favorite: FavoriteCreate, db: Session = Depends(get_db)):
    return add_favorite(db, favorite)

@router.delete("/{favorite_id}", response_model=bool)
def delete_favorite(favorite_id: int, db: Session = Depends(get_db)):
    return remove_favorite(db, favorite_id)

@router.put("/{favorite_id}", response_model=FavoriteRead)
def update_favorite(favorite_id: int, favorite: FavoriteUpdate, db: Session = Depends(get_db)):
    return modify_favorite(db, favorite_id, favorite)

@router.get("/{user_id}", response_model=List[FavoriteRead])
def read_favorites(user_id: int, db: Session = Depends(get_db)):
    return list_favorites(db, user_id)
