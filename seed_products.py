from app.database import SessionLocal, engine
from app import models

db = SessionLocal()

products = [
    # 🐶 Dog Products
    {"name": "Pedigree Adult Dog Food", "brand": "Pedigree", "price": 2599, "stock": 40, "category": "Dog", "description": "Complete nutrition for adult dogs"},
    {"name": "Royal Canin Puppy Formula", "brand": "Royal Canin", "price": 3549, "stock": 30, "category": "Dog", "description": "Supports healthy growth in puppies"},
    {"name": "Purina Pro Plan Lamb & Rice", "brand": "Purina", "price": 2999, "stock": 25, "category": "Dog", "description": "Lamb-based formula for sensitive dogs"},
    {"name": "Jerky Treats", "brand": "Milk-Bone", "price": 849, "stock": 50, "category": "Dog", "description": "Chewy chicken jerky treats for dogs"},
    {"name": "Rope Tug Toy", "brand": "KONG", "price": 1299, "stock": 35, "category": "Dog", "description": "Durable tug toy for playtime"},
    {"name": "Squeaky Ball", "brand": "Nylabone", "price": 999, "stock": 40, "category": "Dog", "description": "Interactive squeaky fetch ball"},
    {"name": "Dog Collar", "brand": "PetSafe", "price": 1449, "stock": 30, "category": "Dog", "description": "Adjustable nylon collar for comfort"},
    {"name": "Dog Shampoo", "brand": "Burt’s Bees", "price": 1149, "stock": 25, "category": "Dog", "description": "Natural dog shampoo for shiny coat"},
    {"name": "Flea Collar", "brand": "Seresto", "price": 3899, "stock": 15, "category": "Dog", "description": "8-month flea and tick protection"},
    {"name": "Dental Chews", "brand": "Greenies", "price": 1949, "stock": 40, "category": "Dog", "description": "Oral care chews for clean teeth"},

    # 🐱 Cat Products
    {"name": "Indoor Cat Formula", "brand": "Whiskas", "price": 2299, "stock": 30, "category": "Cat", "description": "Balanced meal for indoor cats"},
    {"name": "Kitten Growth Formula", "brand": "Royal Canin", "price": 3349, "stock": 25, "category": "Cat", "description": "High-protein food for kittens"},
    {"name": "Tuna & Salmon Delight", "brand": "Purina ONE", "price": 2999, "stock": 20, "category": "Cat", "description": "Grain-free wet cat food"},
    {"name": "Sensitive Stomach Cat Food", "brand": "Hill’s Science Diet", "price": 3499, "stock": 15, "category": "Cat", "description": "For cats with delicate digestion"},
    {"name": "Crunchy Chicken Treats", "brand": "Temptations", "price": 949, "stock": 50, "category": "Cat", "description": "Crispy treats cats love"},
    {"name": "Feather Wand Toy", "brand": "SmartyKat", "price": 899, "stock": 50, "category": "Cat", "description": "Interactive play wand"},
    {"name": "Laser Pointer", "brand": "PetSafe", "price": 749, "stock": 60, "category": "Cat", "description": "Laser toy for cats to chase"},
    {"name": "Cat Collar", "brand": "Rogz", "price": 999, "stock": 30, "category": "Cat", "description": "Safety breakaway collar"},
    {"name": "Scratching Post", "brand": "Frisco", "price": 2799, "stock": 20, "category": "Cat", "description": "Durable post for scratching"},
    {"name": "Hairball Control Supplement", "brand": "VetIQ", "price": 1499, "stock": 25, "category": "Cat", "description": "Reduces hairball formation"},

    # 🐠 Fish Products
    {"name": "Tropical Flake Food", "brand": "TetraMin", "price": 699, "stock": 60, "category": "Fish", "description": "For tropical aquarium fish"},
    {"name": "Goldfish Pellets", "brand": "Aqueon", "price": 549, "stock": 50, "category": "Fish", "description": "Pellets for goldfish"},
    {"name": "Betta Bits", "brand": "Hikari", "price": 499, "stock": 55, "category": "Fish", "description": "Floating pellets for bettas"},
    {"name": "Aquarium Filter", "brand": "AquaClear", "price": 3999, "stock": 15, "category": "Fish", "description": "3-stage filtration system"},
    {"name": "LED Tank Light", "brand": "Fluval", "price": 2999, "stock": 20, "category": "Fish", "description": "Energy-efficient LED lighting"},
    {"name": "Water Conditioner", "brand": "API", "price": 1199, "stock": 25, "category": "Fish", "description": "Removes chlorine and detoxifies water"},
    {"name": "Aquarium Gravel", "brand": "Marina", "price": 1299, "stock": 35, "category": "Fish", "description": "Decorative substrate for tanks"},
    {"name": "Gravel Vacuum", "brand": "Python", "price": 1909, "stock": 25, "category": "Fish", "description": "Easy water changer and cleaner"},
    {"name": "Water Test Kit", "brand": "Tetra", "price": 1649, "stock": 20, "category": "Fish", "description": "Monitors water parameters"},
    {"name": "Tank Wipes", "brand": "Fluval", "price": 800, "stock": 25, "category": "Fish", "description": "Quick wipes for tank cleaning"},
]

for p in products:
    product = models.Product(**p)
    db.add(product)

db.commit()
db.close()
print("✅ Successfully added all products to database!")
