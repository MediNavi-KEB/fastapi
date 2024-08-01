from pydantic import BaseModel

class FavoriteBase(BaseModel):
    name: str
    user_id: int

class FavoriteCreate(FavoriteBase):
    pass

class FavoriteUpdate(FavoriteBase):
    pass

class Favorite(FavoriteBase):
    id: int

    class Config:
        orm_mode: True
