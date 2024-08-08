from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dto.favorite_dto import FavoriteCreateModel, FavoriteUpdateModel
from services import favorite_service
from db.connection import get_db
from typing import List

favorite_router = APIRouter(tags=["Favorites"])


@favorite_router.post("/create", response_model=FavoriteCreateModel)
def create_favorite(favorite: FavoriteCreateModel, db: Session = Depends(get_db)):
    return favorite_service.create_favorite(db, favorite)


@favorite_router.get("/get/{user_id}")
def get_favorites(user_id: str, db: Session = Depends(get_db)):
    return favorite_service.get_favorites(db, user_id)


@favorite_router.delete("/delete/{user_id}/{hospital_name}")
def delete_favorite(user_id: str, hospital_name: str, db: Session = Depends(get_db)):
    return favorite_service.delete_favorite(db, user_id, hospital_name)


@favorite_router.delete("/delete_by_id/{favorite_id}")
def delete_favorite_by_id(favorite_id: int, db: Session = Depends(get_db)):
    return favorite_service.delete_favorite_by_id(db, favorite_id)


@favorite_router.put("/update/{favorite_id}")
def update_favorite(favorite_id: int, favorite_update: FavoriteUpdateModel, db: Session = Depends(get_db)):
    return favorite_service.update_favorite(db, favorite_id, favorite_update)
