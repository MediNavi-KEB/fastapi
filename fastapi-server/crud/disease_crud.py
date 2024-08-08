from sqlalchemy.orm import Session
from db.models.disease import Disease, UserDisease, Department, DiseaseDepartment
from dto.disease_dto import DiseaseModel, DepartmentModel, DiseaseDepartmentModel, UserDiseaseCreateModel, UserDiseaseModel
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import func
from db.models.disease import UserDisease


def get_dept_by_user_disease(db: Session, user_disease: UserDiseaseCreateModel) -> List[Department]:
    disease = db.query(Disease).filter(Disease.disease_name == user_disease.disease_name).first()
    if not disease:
        return []

    department_ids = db.query(DiseaseDepartment.department_id).filter(DiseaseDepartment.disease_id == disease.disease_id).all()
    departments = db.query(Department).filter(Department.department_id.in_([dept_id for dept_id, in department_ids])).all()

    return departments


# 질병이 `diseases` 테이블에 존재하는지 확인
def check_disease_exists(db: Session, disease_name: str):
    return db.query(Disease).filter(Disease.disease_name == disease_name).first()


# `chat_history` 테이블에 데이터 삽입
def add_user_disease(db: Session, user_disease: UserDisease):
    db.add(user_disease)
    db.commit()
    db.refresh(user_disease)
    return user_disease


def get_user_diseases(db: Session, user_id: str, skip: int = 0, limit: int = 5):
    return db.query(UserDisease).filter(UserDisease.user_id == user_id).offset(skip).limit(limit).all()


def get_department_ids_by_disease(db: Session, disease_name: str):
    result = db.query(DiseaseDepartment.department_id)\
               .join(Disease, Disease.disease_id == DiseaseDepartment.disease_id)\
               .filter(Disease.disease_name == disease_name)\
               .all()
    return [r[0] for r in result]


def get_dept_by_disease_name(db: Session, disease_name: str):
    department_ids = get_department_ids_by_disease(db, disease_name)
    if not department_ids:
        return []

    departments = db.query(Department).filter(Department.department_id.in_(department_ids)).all()
    return departments


def get_user_top_disease(db: Session, user_id: str):
    return db.query(UserDisease.disease_name, func.count(UserDisease.disease_name).label('frequency'))\
             .filter(UserDisease.user_id == user_id)\
             .group_by(UserDisease.disease_name)\
             .order_by(func.count(UserDisease.disease_name).desc())\
             .first()


def get_user_disease_frequencies(db: Session, user_id: str):
    return db.query(UserDisease.disease_name, func.count(UserDisease.disease_name).label('frequency'))\
             .filter(UserDisease.user_id == user_id)\
             .group_by(UserDisease.disease_name)\
             .all()
