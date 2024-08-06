from pydantic import BaseModel

class FavoriteCreateModel(BaseModel):
    user_id: str
    hospital_name: str

class FavoriteUpdateModel(BaseModel):
    hospital_name: str
