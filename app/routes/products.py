from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.auth import get_current_user
from app.models import User, Product, ProductOrder
from app.database import get_db

router = APIRouter(prefix="/products", tags=["Shop 🛍️"])

# 🛍️ Get products (with optional filtering)
@router.get("/", response_model=List[dict])
def get_products(
    species: str | None = None,
    brand: str | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(Product)

    # ✅ Flexible, case-insensitive partial match
    if species:
        query = query.filter(Product.species.ilike(f"%{species}%"))
    if brand:
        query = query.filter(Product.brand.ilike(f"%{brand}%"))

    products = query.all()

    return [
        {
            "id": p.id,
            "name": p.name,
            "description": p.description,
            "price": p.price,
            "stock": p.stock,
            "brand": p.brand,
            "species": p.species,  
            "category": p.category,
        }
        for p in products
    ]


# 🧑‍💼 Admin: Add new product
@router.post("/", response_model=dict)
def create_product(
    data: dict,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admin users can add products",
        )

    if not all(k in data for k in ["name", "price", "stock"]):
        raise HTTPException(status_code=400, detail="Missing required fields")

    product = Product(**data)
    db.add(product)
    db.commit()
    db.refresh(product)

    return {"message": "Product added successfully", "product_id": product.id}


# 🛒 Place an order
@router.post("/order", response_model=dict)
def order_product(
    data: dict,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    product_id = data.get("product_id")
    quantity = data.get("quantity", 1)

    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.stock < quantity:
        raise HTTPException(status_code=400, detail="Not enough stock available")

    total_price = product.price * quantity
    product.stock -= quantity

    order = ProductOrder(
        user_id=current_user.id,
        product_id=product.id,
        quantity=quantity,
        total_price=total_price,
    )

    db.add(order)
    db.commit()

    return {
        "message": "Order placed successfully",
        "user": current_user.username,
        "product": product.name,
        "quantity": quantity,
        "total_price": total_price,
    }


# 🧾 Get my orders
@router.get("/orders/me", response_model=list)
def get_my_orders(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    orders = db.query(ProductOrder).filter(ProductOrder.user_id == current_user.id).all()

    return [
        {
            "order_id": o.id,
            "product_id": o.product_id,
            "quantity": o.quantity,
            "total_price": o.total_price,
        }
        for o in orders
    ]
