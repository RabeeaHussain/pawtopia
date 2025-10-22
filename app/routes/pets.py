from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models
from app.database import get_db
from app.auth import get_current_user
from app.models import User

router = APIRouter(prefix="/pets", tags=["Pets 🐶"])

# ---------------- List available pets ----------------
@router.get("/")
def list_all_pets(db: Session = Depends(get_db)):
    pets = db.query(models.Pet).all()
    return [
        {
            "id": pet.id,
            "name": pet.name,
            "species": pet.species,
            "age": pet.age,
            "description": pet.description,
            "price": pet.price,
            "is_adopted": pet.is_adopted
        }
        for pet in pets
    ]


# ---------------- Add new pet (admin use) ----------------
@router.post("/")
def add_pet(
    name: str,
    species: str,
    price: float,
    age: int = None,
    description: str = None,
    db: Session = Depends(get_db)
):
    """
    Admin route — add a new real pet for adoption.
    """
    pet = models.Pet(
        name=name,
        species=species,
        price=price,
        age=age,
        description=description,
        is_adopted=False
    )
    db.add(pet)
    db.commit()
    db.refresh(pet)
    return pet


# ---------------- Adopt a real pet ----------------
@router.post("/{pet_id}/adopt")
def adopt_real_pet(
    pet_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Adopt (purchase) a real pet.
    """
    pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    if pet.is_adopted:
        raise HTTPException(status_code=400, detail="Pet already adopted")

    pet.is_adopted = True
    pet.owner_id = current_user.id
    db.commit()
    db.refresh(pet)

    return {
        "message": f"Congratulations! You adopted {pet.name} 🐾",
        "pet": {
            "id": pet.id,
            "name": pet.name,
            "species": pet.species,
            "price": pet.price,
            "is_adopted": pet.is_adopted,
        },
    }


# ---------------- Get my adopted pets ----------------
@router.get("/my")
def my_adopted_pets(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    pets = db.query(models.Pet).filter(models.Pet.owner_id == current_user.id).all()
    return pets

@router.post("/{pet_id}/unadopt")
def unadopt_pet(pet_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    pet = db.query(models.Pet).filter(models.Pet.id == pet_id, models.Pet.owner_id == current_user.id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found or not adopted by you")
    pet.is_adopted = False
    pet.owner_id = None
    db.commit()
    return {"message": f"{pet.name} has been unadopted"}
