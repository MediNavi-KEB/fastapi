from pydantic import BaseModel


class FavoriteCreateModel(BaseModel):
    user_id: str
    hospital_name: str
    hospital_address: str
    hospital_phone: str


class FavoriteUpdateModel(BaseModel):
    hospital_name: str
    hospital_address: str
    hospital_phone: str
