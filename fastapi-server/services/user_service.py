from sqlalchemy.orm import Session
from crud.user_crud import create_user, get_user_by_id
from dto.user_dto import UserCreateModel, UserLoginModel
from fastapi import HTTPException

def register_user(db: Session, user: UserCreateModel):
    db_user = get_user_by_id(db, user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return create_user(db, user)

def login_user(db: Session, user: UserLoginModel):
    db_user = get_user_by_id(db, user.id)
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message" : "로그인 성공"}
