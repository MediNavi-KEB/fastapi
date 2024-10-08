from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dto.user_dto import UserCreateModel, UserLoginModel, UserUpdateModel, UserIdCheckModel, ChatDescriptionUpdateModel
from services import user_service
from db.connection import get_db

user_router = APIRouter(tags=["User"])


@user_router.post("/register", response_model=UserCreateModel)
def register(user: UserCreateModel, db: Session = Depends(get_db)):
    return user_service.register_user(db, user)


@user_router.post("/login")
def login(user: UserLoginModel, db: Session = Depends(get_db)):
    return user_service.login_user(db, user)


@user_router.delete("/delete/{user_id}")
def delete(user_id: str, db: Session = Depends(get_db)):
    return user_service.delete_user(db, user_id)


@user_router.put("/update/{user_id}")
def update(user_id: str, user_update: UserUpdateModel, db: Session = Depends(get_db)):
    return user_service.update_user(db, user_id, user_update)


@user_router.post("/id-check")
def check_id(request: UserIdCheckModel, db:Session = Depends(get_db)):
    exists = user_service.check_duplicate_id(db, request.user_id)
    return {"exists" : exists}


@user_router.get("/get/{user_id}")
def get_user(user_id: str, db: Session = Depends(get_db)):
    return user_service.get_user(db, user_id)


@user_router.put("/update/chat_description/{user_id}")
def update_chat_description(user_id: str, chat_description: ChatDescriptionUpdateModel, db: Session = Depends(get_db)):
    return user_service.update_chat_description(db, user_id, chat_description.chat_description)
