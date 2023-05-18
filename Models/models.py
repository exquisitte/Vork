from pydantic import BaseModel, EmailStr
from typing import List, Optional


class Token(BaseModel):
    access_token: str
    token_type: str


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


class Vacancions(BaseModel):
    employee_email: EmailStr
    city: str
    company_name: str
    vacancion_name: str
    money: Optional[float]
    employment_type: str
    needed_experience: List[str]
    description: str


class Filters(BaseModel):
    min_money: int
    max_money: int
    country: Optional[str]
    region: Optional[str]
    work: Optional[str]
    employment_type: Optional[List[str]]
    experience: Optional[List[str]]



