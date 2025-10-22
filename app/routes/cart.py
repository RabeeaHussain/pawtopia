from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_current_user
from app import models
from app.models import User, CartItem, Product 

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.post("/add/{pet_id}")
def add_to_cart(pet_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    if pet.is_adopted:
        raise HTTPException(status_code=400, detail="Pet already adopted")

    # Check if already in cart
    existing = db.query(models.CartItem).filter_by(user_id=current_user.id, pet_id=pet_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Pet already in cart")

    cart_item = models.CartItem(user_id=current_user.id, pet_id=pet.id, quantity=1, price=pet.price)
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)

    return {"message": f"{pet.name} added to cart!"}

@router.delete("/remove/{item_id}")
def remove_cart_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    cart_item = db.query(models.CartItem).filter(
        models.CartItem.id == item_id,
        models.CartItem.user_id == current_user.id
    ).first()

    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    db.delete(cart_item)
    db.commit()
    return {"message": "Item removed from cart"}

@router.get("/")
def view_cart(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    try:
        items = db.query(models.CartItem).filter_by(user_id=current_user.id).all()
        cart_data = []
        for i in items:
            # Handle both pet and product items
            name = i.pet.name if i.pet else i.product.name
            cart_data.append({
                "id": i.id,
                "pet_id": i.pet_id,
                "product_id": i.product_id,
                "name": name,
                "price": i.price,
                "quantity": i.quantity
            })
        total = sum(i["price"] * i["quantity"] for i in cart_data)
        return {"cart": cart_data, "total": total}
    except Exception as e:
        print("Cart fetch error:", e)
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/checkout")
def checkout_cart(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    cart_items = db.query(models.CartItem).filter(models.CartItem.user_id == current_user.id).all()
    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    total_amount = 0.0
    for item in cart_items:
        total_amount += item.price * item.quantity

        # Optionally reduce stock for products
        if item.product_id:
            product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
            if product:
                if product.stock < item.quantity:
                    raise HTTPException(status_code=400, detail=f"Not enough stock for {product.name}")
                product.stock -= item.quantity

    # Clear cart
    for item in cart_items:
        db.delete(item)
    
    db.commit()
    return {"message": f"Checkout successful. Total amount: ${total_amount}"}

@router.post("/add_product/{product_id}")
def add_product_to_cart(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.stock < 1:
        raise HTTPException(status_code=400, detail="Product out of stock")
    
    # Check if already in cart
    existing = (
        db.query(models.CartItem)
        .filter_by(user_id=current_user.id, product_id=product_id)
        .first()
    )
    if existing:
        existing.quantity += 1
        db.commit()
        db.refresh(existing)
        return {"message": f"{product.name} quantity increased in cart", "cart_item": existing}

    # Add new cart item
    cart_item = models.CartItem(
        user_id=current_user.id,
        product_id=product.id,
        pet_id=None,  
        quantity=1,
        price=product.price
    )
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return {"message": f"{product.name} added to cart", "cart_item": cart_item}
