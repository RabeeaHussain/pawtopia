from datetime import datetime, timezone
from app import models
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Templates
pets = [
    {"name": "Pixel", "species": "Dog", "base_hunger": 70, "base_happiness": 85, "base_energy": 60},
    {"name": "Whiskers", "species": "Cat", "base_hunger": 50, "base_happiness": 90, "base_energy": 70},
    {"name": "Bubbles", "species": "Fish", "base_hunger": 80, "base_happiness": 65, "base_energy": 55},
    {"name": "Luna", "species": "Dog", "base_hunger": 40, "base_happiness": 95, "base_energy": 80},
    {"name": "Mochi", "species": "Cat", "base_hunger": 60, "base_happiness": 70, "base_energy": 50},
]

for t in pets:
    db.add(models.VirtualPet(**t))

db.commit()
db.close()
print("✅ Virtual pet templates seeded successfully!")