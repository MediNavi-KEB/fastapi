from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dto.disease_dto import DiseaseModel, UserDiseaseCreateModel, DepartmentModel, UserDiseaseModel
from services import disease_service
from db.connection import get_db

disease_router = APIRouter(tags=["Disease"])


# 사용자의 질병을 저장하는 라우트
@disease_router.post("/user_disease", response_model=list[DepartmentModel])
def create_user_disease(user_disease: UserDiseaseCreateModel, db: Session = Depends(get_db)):
    # 사용자의 질병을 저장
    disease_service.create_user_disease(db, user_disease)
    # 저장한 질병 정보로 부서를 조회
    return disease_service.get_dept(db, user_disease)


@disease_router.get("/user_disease/{user_id}", response_model=list[UserDiseaseModel])
def get_user_disease_history(user_id: str, db: Session = Depends(get_db)):
    return disease_service.get_userDisease(db, user_id)


@disease_router.get("/department_by_disease/{disease_name}")
def get_department_by_disease(disease_name: str, db: Session = Depends(get_db)):
    try:
        departments = disease_service.get_department_by_disease(db, disease_name)
        if not departments:
            raise HTTPException(status_code=404, detail="해당 질병에 대한 진료과 정보가 없습니다.")
        return departments
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
