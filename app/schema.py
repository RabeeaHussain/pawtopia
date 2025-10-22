from pydantic import BaseModel, EmailStr


# ---- Base Schemas ----

class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str


# ---- Request Schemas ----

class UserCreate(UserBase):
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


# ---- Response Schemas ----

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

class PetCreate(BaseModel):
    name: str
    species: str  # ✅ must be included!

class VirtualPetBase(BaseModel):
    name: str
    species: str
    hunger: int
    happiness: int
    energy: int

class PetOut(BaseModel):
    id: int
    name: str
    type: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str


class CartItemOut(BaseModel):
    id: int
    user_id: int
    pet_id: int | None
    product_id: int | None
    quantity: int
    price: float

    class Config:
        orm_mode = True
