from pydantic import BaseModel
from typing import Optional

class UserCreateModel(BaseModel):
    id: str
    password: str
    name: str
    phone: Optional[str]
    email: Optional[str]
    address: Optional[str]
    gender: Optional[str]

class UserLoginModel(BaseModel):
    id: str
    password: str
