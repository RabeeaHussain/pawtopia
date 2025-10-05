from fastapi import FastAPI
from app import models
from app.database import engine
from app.routes import pets, users, orders, products

print("Creating all tables now...")
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Register pets routes
app.include_router(pets.router)
app.include_router(users.router)
app.include_router(orders.router)
app.include_router(products.router)

@app.get("/")
def root():
    return {"message": "Welcome to Pawtopia 🐾"}
