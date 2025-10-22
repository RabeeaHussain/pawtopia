from app import models
from app.database import SessionLocal, engine

# Make sure tables exist
models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

pets = [
    {"name": "Milo", "species": "Cat", "age": 2, "description": "Playful and loves naps", "price": 12000},
    {"name": "Bella", "species": "Dog", "age": 3, "description": "Friendly golden retriever", "price": 25000},
    {"name": "Charlie", "species": "Dog", "age": 1, "description": "Energetic and curious", "price": 18000},
    {"name": "Luna", "species": "Cat", "age": 4, "description": "Calm and affectionate", "price": 15000},
    {"name": "Goldie", "species": "Fish", "age": 1, "description": "A shiny goldfish that brightens the tank", "price": 3000},
]

for p in pets:
    pet = models.Pet(**p)
    db.add(pet)

db.commit()
db.close()

print("✅ Pets seeded successfully with price in rupees!")
