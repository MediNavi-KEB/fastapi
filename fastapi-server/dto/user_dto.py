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

class UserDeleteModel(BaseModel):
    id: str
    password: str

class UserUpdateModel(BaseModel):
    id: str
    password: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    gender: Optional[str] = None
