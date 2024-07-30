from pydantic import BaseModel

class FavoriteCreate(BaseModel):
    user_id: int
    hospital_id: int

class FavoriteUpdate(BaseModel):
    hospital_id: int

class FavoriteRead(BaseModel):
    id: int
    user_id: int
    hospital_id: int

    class Config:
        from_attributes = True  # 여기를 orm_mode에서 from_attributes로 변경합니다.
