from sqlalchemy.orm import Session
from db.models.user import User
from dto.user_dto import UserCreateModel

def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreateModel):
    db_user = User(
        id=user.id,
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
