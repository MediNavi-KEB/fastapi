from pydantic import BaseModel


class FavoriteCreateModel(BaseModel):
    user_id: str
    hospital_name: str
    hospital_address: str
    hospital_phone: str
    latitude: str
    longitude: str
    category: str


class FavoriteUpdateModel(BaseModel):
    hospital_name: str
    hospital_address: str
    hospital_phone: str
    latitude: str
    longitude: str
    category: str
