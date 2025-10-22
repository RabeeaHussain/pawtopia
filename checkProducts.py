from app.database import SessionLocal
from app.models import Product

db = SessionLocal()

products = db.query(Product).all()

if not products:
    print("⚠️ No products found in database.")
else:
    for p in products:
        print(f"ID: {p.id}, Name: {p.name}, Species: {p.species}, Brand: {p.brand}")
