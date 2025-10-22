from fastapi import FastAPI
from app import models
from app.database import engine
from app.routes import pets, users,products,virtual_pets,cart
from fastapi.middleware.cors import CORSMiddleware


print("Connecting to database...")
models.Base.metadata.create_all(bind=engine)
print("✅ Connected successfully.")


app = FastAPI()

origins = [
    "http://localhost:5173",  # Vite default
    "http://127.0.0.1:5173",  # Some browsers use this variant
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],            # Allow all HTTP methods
    allow_headers=["*"],            # Allow all headers
)

# Register pets routes
app.include_router(pets.router)
app.include_router(users.router)
app.include_router(products.router)
app.include_router(virtual_pets.router)
app.include_router(cart.router)



@app.get("/")
def root():
    return {"message": "Welcome to Pawtopia 🐾"}

