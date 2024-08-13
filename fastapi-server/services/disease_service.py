from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List
from crud import disease_crud
from db.models.disease import Disease, UserDisease, Department, DiseaseDepartment
from dto.disease_dto import DiseaseModel, DepartmentModel, DiseaseDepartmentModel, UserDiseaseCreateModel, UserDiseaseModel
from sqlalchemy.orm import Session
from crud import disease_crud




# 1. get_dept_by_name을 통해 질병을 입력했을 때 해당 진료과가 나오도록 하고 없으면 없다는 것을 출력
# 2. user_disease 테이블을 통해 해당 user가 가진 정보를 입력했을 때 disease 정보가 있는지 확인 없다면 질병내역이 없음을 출력
# 3. user_disaes를 DB에 저장하고 저장실패및 성공을 알림
# 4. 삭제가 성공한지 실패인지를 알림
def get_dept(db: Session, user_disease: UserDiseaseCreateModel) -> List[DepartmentModel]:
    db_diseaseDept = disease_crud.get_dept_by_user_disease(db, user_disease)
    if not db_diseaseDept:
        raise HTTPException(status_code=400, detail="해당 질병에 대한 진료과 정보가 없습니다.")
    return [DepartmentModel.from_orm(dept) for dept in db_diseaseDept]


# def get_userDisease(db: Session, user_id: str):
#     db_userDisease = disease_crud.get_user_diseases(db, user_id)
#     if not db_userDisease:
#         raise HTTPException(status_code=400, detail="해당 사용자에 대한 질병 기록이 없습니다.")
#     return db_userDisease

def create_user_disease(db: Session, user_disease: UserDiseaseCreateModel):
    # 질병이 존재하는지 확인
    if not disease_crud.check_disease_exists(db, user_disease.disease_name):
        raise HTTPException(status_code=400, detail=f"질병 정보가 존재하지 않습니다: {user_disease.disease_name}")

    db_user_disease = UserDisease(
        user_id=user_disease.user_id,
        disease_name=user_disease.disease_name,
        date_time=user_disease.date_time
    )

    added_disease = disease_crud.add_user_disease(db, db_user_disease)
    return {"message": "질병 정보가 성공적으로 저장되었습니다.", "data": added_disease}


def get_department_by_disease(db: Session, disease_name: str):
    return disease_crud.get_dept_by_disease_name(db, disease_name)


def fetch_user_top_disease(db: Session, user_id: str):
    return disease_crud.get_user_top_disease(db, user_id)


def fetch_user_disease_frequencies(db: Session, user_id: str):
    diseases = disease_crud.get_user_disease_frequencies(db, user_id)
    return [{"name": disease, "frequency": freq} for disease, freq in diseases]


def get_recent_disease_data(db: Session, user_id: str):
    return disease_crud.get_recent_disease_data(db, user_id)


def get_disease_description(db: Session, disease_name: str):
    return disease_crud.get_disease_description(db, disease_name)


def get_disease_icon(db: Session, disease_name: str):
    return disease_crud.get_disease_icon(db, disease_name)
