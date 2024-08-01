from pydantic import BaseModel
from datetime import datetime

class DiseaseModel(BaseModel):
    disease_id: int
    disease_name: str

    class Config:
        from_attributes = True


class DepartmentModel(BaseModel):
    department_id: int
    department_name: str

    class Config:
        from_attributes = True


class DiseaseDepartmentModel(BaseModel):
    department_id: int
    disease_id: int

    class Config:
        from_attributes = True


class UserDiseaseCreateModel(BaseModel):
    user_id: str
    disease_name: str
    date_time: datetime


class UserDiseaseModel(BaseModel):
    ch_id: int
    user_id: str
    disease_name: str
    date_time: datetime

    class Config:
        from_attributes = True
