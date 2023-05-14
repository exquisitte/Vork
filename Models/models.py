from pydantic import BaseModel, EmailStr
from typing import List
from fastapi import UploadFile


class User_reg(BaseModel):
    name: str
    email: EmailStr
    description: str
    skills: List[str]
    exp: List[str]
    living_place: str
    password: str


class User_login(BaseModel):
    email: EmailStr
    password: str


class UserInDB(User_reg):
    hashed_password: str