from sqlalchemy.orm import Session
from db.models.disease import Disease, UserDisease, Department, DiseaseDepartment
from dto.disease_dto import DiseaseModel, DepartmentModel, DiseaseDepartmentModel, UserDiseaseCreateModel, UserDiseaseModel
from typing import List

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
