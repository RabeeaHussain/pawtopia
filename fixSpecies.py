from app.database import SessionLocal
from app.models import Product

db = SessionLocal()

# Define simple rules
dog_keywords = ["dog", "puppy", "bone", "chew", "tug", "kong"]
cat_keywords = ["cat", "kitten", "whiskas", "temptations", "feather", "laser"]
fish_keywords = ["fish", "aquarium", "tank", "betta", "goldfish", "water"]

products = db.query(Product).all()

for p in products:
    name_lower = p.name.lower()
    if any(word in name_lower for word in dog_keywords):
        p.species = "dog"
    elif any(word in name_lower for word in cat_keywords):
        p.species = "cat"
    elif any(word in name_lower for word in fish_keywords):
        p.species = "fish"
    else:
        p.species = "other"

db.commit()
db.close()

print("✅ Species fields updated successfully!")
