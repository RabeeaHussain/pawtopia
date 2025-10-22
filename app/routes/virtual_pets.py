from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_current_user
from app import models

router = APIRouter(prefix="/virtual_pets", tags=["Virtual Pets 🐾"])

@router.get("/", response_model=dict)
def get_virtual_pets(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    templates = db.query(models.VirtualPet).all()

    # All adopted by this user
    adopted = db.query(models.UserVirtualPet).filter_by(user_id=current_user.id).all()
    adopted_ids = {p.virtual_pet_id for p in adopted}

    available = [
        {
            "id": t.id,
            "name": t.name,
            "species": t.species,
            "hunger": t.base_hunger,
            "happiness": t.base_happiness,
            "energy": t.base_energy
        }
        for t in templates if t.id not in adopted_ids
    ]

    adopted_list = [
        {
            "id": p.id,
            "name": p.virtual_pet.name,
            "species": p.virtual_pet.species,
            "hunger": p.hunger,
            "happiness": p.happiness,
            "energy": p.energy
        }
        for p in adopted
    ]

    return {"available": available, "adopted": adopted_list}


@router.post("/adopt/{pet_id}")
def adopt_pet(pet_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    # Prevent duplicate adoption
    exists = db.query(models.UserVirtualPet).filter_by(user_id=current_user.id, virtual_pet_id=pet_id).first()
    if exists:
        raise HTTPException(status_code=400, detail="Pet already adopted")

    pet_template = db.query(models.VirtualPet).filter_by(id=pet_id).first()
    if not pet_template:
        raise HTTPException(status_code=404, detail="Pet not found")

    user_pet = models.UserVirtualPet(
        user_id=current_user.id,
        virtual_pet_id=pet_template.id,
        hunger=pet_template.base_hunger,
        happiness=pet_template.base_happiness,
        energy=pet_template.base_energy,
        
    )
    db.add(user_pet)
    db.commit()
    db.refresh(user_pet)

    return {"message": f"You adopted {pet_template.name}!"}
