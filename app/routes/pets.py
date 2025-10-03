from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models
from app.database import get_db

# ✅ Correct: use APIRouter
router = APIRouter(prefix="/pets", tags=["Pets"])

@router.get("/")
def list_pets(db: Session = Depends(get_db)):
    return db.query(models.Pet).filter(models.Pet.available == 1).all()

@router.post("/")
def add_pet(name: str, species: str, price: float, db: Session = Depends(get_db)):
    pet = models.Pet(name=name, species=species, price=price)
    db.add(pet)
    db.commit()
    db.refresh(pet)
    return pet

@router.post("/{pet_id}/adopt")
def adopt_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(models.Pet).filter(models.Pet.id == pet_id, models.Pet.available == 1).first()
    if not pet:
        return {"error": "Pet not available"}
    pet.available = 0
    db.commit()
    return {"message": f"{pet.name} has been adopted!"}
