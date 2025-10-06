# schemas.py
from pydantic import BaseModel, EmailStr
from datetime import datetime


# ----- User Schemas -----
class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


# ----- Auth Schema -----
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ----- Order Schemas -----
class OrderBase(BaseModel):
    amount: float


class OrderCreate(OrderBase):
    pass


class OrderResponse(OrderBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
