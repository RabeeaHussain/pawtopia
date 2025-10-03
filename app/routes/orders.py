# routes/orders.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Order, User
from app.schema import OrderCreate, OrderResponse
from app.auth import decode_access_token

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=OrderResponse)
def create_order(
    order: OrderCreate, 
    db: Session = Depends(get_db), 
    token_data: dict = Depends(decode_access_token)
    ):
    user_id = int(token_data["sub"])
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_order = Order(user_id=user.id, amount=order.amount)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


@router.get("/", response_model=list[OrderResponse])
def get_orders(
    db: Session = Depends(get_db), 
    token_data: dict = Depends(decode_access_token)
    ):
    user_id = int(token_data["sub"])
    orders = db.query(Order).filter(Order.user_id == user_id).all()
    return orders
