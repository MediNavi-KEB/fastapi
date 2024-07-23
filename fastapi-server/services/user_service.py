from sqlalchemy.orm import Session
from crud.user_crud import create_user, get_user_by_id
from dto.user_dto import UserCreateModel, UserLoginModel, UserUpdateModel, UserDeleteModel
from fastapi import HTTPException
from db.models.user import User

def register_user(db: Session, user: UserCreateModel):
    db_user = get_user_by_id(db, user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="이미 존재하는 아이디입니다.")
    return create_user(db, user)

def login_user(db: Session, user: UserLoginModel):
    db_user = get_user_by_id(db, user.id)
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=400, detail="비밀번호가 일치하지 않습니다.")
    return {"message" : "로그인 성공"}

def delete_user(db: Session, user: UserDeleteModel):
    db_user = get_user_by_id(db, user.id)
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=400, detail="비밀번호가 일치하지 않습니다.")



    db.delete(db_user)
    db.commit()

    return{"message" : "아이디가 삭제되었습니다."}

def update_user(db: Session, user_id: str, user_update: UserUpdateModel):
    db_user = get_user_by_id(db, user_id)

    if db_user is None:
        raise HTTPException(status_code=400, detail="아이디를 찾을 수 없습니다.")
    if user_update.id is not None and user_update.id != user_id:
        raise HTTPException(status_code=400, detail="아이디는 변경할 수 없습니다.")

    if user_update.password is not None:
        db_user.password = user_update.password
    if user_update.name is not None:
        db_user.name = user_update.name
    if user_update.phone is not None:
        db_user.phone = user_update.phone
    if user_update.address is not None:
        db_user.address = user_update.address
    if user_update.email is not None:
        db_user.email = user_update.email
    if user_update.gender is not None:
        db_user.gender = user_update.gender

    db.commit()
    db.refresh(db_user)
    return{"message" : "수정이 완료되었습니다."}

