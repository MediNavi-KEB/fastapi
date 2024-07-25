from sqlalchemy.orm import Session
from db.models.user import User
from dto.user_dto import UserCreateModel, UserUpdateModel


def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.user_id == user_id).first()


def create_user(db: Session, user: UserCreateModel):
    db_user = User(
        user_id=user.user_id,
        password=user.password,
        name=user.name,
        phone=user.phone,
        email=user.email,
        address=user.address,
        gender=user.gender
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id : str):
    db_user = get_user_by_id(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user


def update_user_db(db: Session, db_user: User, user_update: UserUpdateModel):
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
    return db_user
