from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import models
from app.database import get_db

router = APIRouter(prefix="/products", tags=["Shop 🛍️"])


# Get all products
@router.get("/", response_model=List[dict])
def get_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return [
        {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "stock": p.stock,
            "brand": p.brand,
        }
        for p in products
    ]


# Add new product (for admin)
@router.post("/", response_model=dict)
def create_product(data: dict, db: Session = Depends(get_db)):
    if not all(k in data for k in ["name", "price", "stock"]):
        raise HTTPException(status_code=400, detail="Missing fields")

    product = models.Product(**data)
    db.add(product)
    db.commit()
    db.refresh(product)
    return {"message": "Product added successfully", "product_id": product.id}


# Place order for a product
@router.post("/order", response_model=dict)
def order_product(data: dict, db: Session = Depends(get_db)):
    product_id = data.get("product_id")
    quantity = data.get("quantity", 1)
    user_id = data.get("user_id", 1)  # 🔹 Replace with real user later

    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.stock < quantity:
        raise HTTPException(status_code=400, detail="Not enough stock available")

    total_price = product.price * quantity
    product.stock -= quantity

    order = models.ProductOrder(
        user_id=user_id,
        product_id=product.id,
        quantity=quantity,
        total_price=total_price,
    )

    db.add(order)
    db.commit()

    return {
        "message": "Order placed successfully",
        "product": product.name,
        "quantity": quantity,
        "total_price": total_price,
    }
