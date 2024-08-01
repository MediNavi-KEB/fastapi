from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.connection import get_db
from services.favorite_service import get_favorite_service, create_favorite_service, get_favorites_service, update_favorite_service, delete_favorite_service
from dto.favorite_dto import FavoriteCreate, FavoriteUpdate, Favorite

favorite_router = APIRouter(tags=["Favorite"])

@favorite_router.get("/{favorite_id}", response_model=Favorite)
def read_favorite(favorite_id: int, db: Session = Depends(get_db)):
    favorite = get_favorite_service(db, favorite_id)
    if favorite is None:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return favorite

@favorite_router.post("/", response_model=Favorite)
def create_favorite(favorite: FavoriteCreate, db: Session = Depends(get_db)):
    return create_favorite_service(db, favorite)

@favorite_router.get("/", response_model=list[Favorite])
def read_favorites(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    favorites = get_favorites_service(db, skip=skip, limit=limit)
    return favorites

@favorite_router.put("/{favorite_id}", response_model=Favorite)
def update_favorite(favorite_id: int, favorite: FavoriteUpdate, db: Session = Depends(get_db)):
    updated_favorite = update_favorite_service(db, favorite_id, favorite)
    if updated_favorite is None:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return updated_favorite

@favorite_router.delete("/{favorite_id}", response_model=Favorite)
def delete_favorite(favorite_id: int, db: Session = Depends(get_db)):
    deleted_favorite = delete_favorite_service(db, favorite_id)
    if deleted_favorite is None:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return deleted_favorite
