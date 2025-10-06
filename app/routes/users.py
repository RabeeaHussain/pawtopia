# routes/users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schema import UserCreate, UserResponse, Token
from app.auth import create_access_token

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/create", response_model=UserResponse)
def create_normal_user(user: UserCreate, db: Session = Depends(get_db)):
    """Register a normal (non-admin) user"""
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(username=user.username, email=user.email)
    new_user.set_password(user.password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    is_admin = user.email.lower() == "rabeeahussain2@gmail.com"

    new_user = User(
        
        username=user.username,
        email=user.email,
        is_admin=is_admin,

    )
    new_user.set_password(user.password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login", response_model=Token)
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not db_user.check_password(user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token({"sub": str(db_user.id)})
    return {"access_token": access_token, "token_type": "bearer"}
