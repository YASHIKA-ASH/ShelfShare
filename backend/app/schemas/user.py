from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):

    full_name: str

    email: EmailStr

    password: str

    phone: Optional[str] = None

    role: str = "Student"


class UserResponse(BaseModel):

    id: int

    full_name: str

    email: EmailStr

    phone: Optional[str]

    role: str

    class Config:
        from_attributes = True


class UserLogin(BaseModel):

    email: EmailStr

    password: str


class Token(BaseModel):

    access_token: str

    token_type: str