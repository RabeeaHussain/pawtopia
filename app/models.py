from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(120), unique=True, nullable=False, index=True)
    password_hash = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_admin = Column(Integer, default=0)

    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")

    # Utility methods
    def set_password(self, password: str):
        self.password_hash = pwd_context.hash(password)

    def check_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password_hash)


# Pet model
class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    # Relationship to orders
    orders = relationship("Order", back_populates="pet", cascade="all, delete-orphan")


# Order model
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Foreign keys
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)

    # Relationships
    user = relationship("User", back_populates="orders")
    pet = relationship("Pet", back_populates="orders")

# 🛍️ Product model (for the shop)
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    brand = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship to product orders
    product_orders = relationship("ProductOrder", back_populates="product", cascade="all, delete-orphan")


# 🧾 ProductOrder model (each entry = one product bought by a user)
class ProductOrder(Base):
    __tablename__ = "product_orders"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Foreign keys
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    quantity = Column(Integer, nullable=False, default=1)
    total_price = Column(Float, nullable=False)

    # Relationships
    user = relationship("User")
    product = relationship("Product", back_populates="product_orders")
