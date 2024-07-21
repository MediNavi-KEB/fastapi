from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dto.user_dto import UserCreateModel, UserLoginModel
from services import user_service
from db.connection import get_db

user_router = APIRouter(tags=["User"])


@user_router.post("/register", response_model=UserCreateModel)
def register(user: UserCreateModel, db: Session = Depends(get_db)):
    return user_service.register_user(db, user)


@user_router.post("/login")
def login(user: UserLoginModel, db: Session = Depends(get_db)):
    return user_service.login_user(db, user)
