from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from app.database import Base
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ------------------ USER MODEL ------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(120), unique=True, nullable=False, index=True)
    password_hash = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_admin = Column(Boolean, default=False)

    # Relationships
    product_orders = relationship("ProductOrder", back_populates="user", cascade="all, delete-orphan")
    adopted_pets = relationship(
        "UserVirtualPet",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    cart_items = relationship("CartItem", back_populates="user", cascade="all, delete-orphan")


    def set_password(self, password: str):
        self.password_hash = pwd_context.hash(password)

    def check_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password_hash)


# ------------------ PET MODEL (for display/catalog only) ------------------
class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False, default=0.0)
    is_adopted = Column(Boolean, default=False)

    # optional: link to user who adopted it
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)

# ------------------ PRODUCT MODEL ------------------
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    brand = Column(String)
    category = Column(String, nullable=False)
    description = Column(String(255))
    species = Column(String, nullable=True)

    product_orders = relationship("ProductOrder", back_populates="product", cascade="all, delete-orphan")


# ------------------ PRODUCT ORDER MODEL ------------------
class ProductOrder(Base):
    __tablename__ = "product_orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, default=1)
    total_price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="product_orders")
    product = relationship("Product", back_populates="product_orders")


# ------------------ VIRTUAL PET MODEL ------------------
class VirtualPet(Base):
    __tablename__ = "virtual_pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    base_hunger = Column(Integer, default=50)
    base_happiness = Column(Integer, default=50)
    base_energy = Column(Integer, default=50)

    adopted_by = relationship(
        "UserVirtualPet",
        back_populates="virtual_pet",
        cascade="all, delete-orphan"
    )

class UserVirtualPet(Base):
    __tablename__ = "user_virtual_pets"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    virtual_pet_id = Column(Integer, ForeignKey("virtual_pets.id"))
    hunger = Column(Integer, default=50)
    happiness = Column(Integer, default=50)
    energy = Column(Integer, default=50)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    user = relationship("User", back_populates="adopted_pets")
    virtual_pet = relationship("VirtualPet", back_populates="adopted_by")

class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=True)
    quantity = Column(Integer, default=1)
    price = Column(Float, nullable=False)

    user = relationship("User", back_populates="cart_items")
    pet = relationship("Pet")
    product = relationship("Product")
