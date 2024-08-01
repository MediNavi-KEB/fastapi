from sqlalchemy.orm import Session
from crud import user_crud
from dto.user_dto import UserCreateModel, UserLoginModel, UserUpdateModel
from fastapi import HTTPException
from db.models.user import User


def register_user(db: Session, user: UserCreateModel):
    db_user = user_crud.get_user_by_id(db, user.user_id)
    if db_user:
        raise HTTPException(status_code=400, detail="이미 존재하는 아이디입니다.")
    return user_crud.create_user(db, user)


def login_user(db: Session, user: UserLoginModel):
    db_user = user_crud.get_user_by_id(db, user.user_id)
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=400, detail="비밀번호가 일치하지 않습니다.")
    return {"message" : "로그인 성공"}


def delete_user(db: Session, user_id: str):
    db_user = user_crud.delete_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="이미 없는 사용자입니다.")
    return db_user


def update_user(db: Session, user_id: str, user_update: UserUpdateModel):
    db_user = user_crud.get_user_by_id(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=400, detail="아이디를 찾을 수 없습니다.")
    return user_crud.update_user_db(db, db_user, user_update)


def check_duplicate_id(db: Session, user_id : str):
    db_user = user_crud.get_user_by_id(db, user_id)
    return db_user is not None


def get_user(db: Session, user_id: str):
    db_user = user_crud.get_user_by_id(db, user_id)
    return db_user
