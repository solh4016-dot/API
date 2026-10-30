"""US09/US10 mantienen su contrato; US12 almacena las operaciones consultables."""
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Cart, CartLine
from ..dependencies import authorized_reader

router = APIRouter(prefix='/carts', tags=['Carritos'])

class CartProduct(BaseModel):
    productId: int = Field(gt=0)
    quantity: int = Field(gt=0)

class CartPayload(BaseModel):
    userId: int = Field(gt=0)
    date: datetime
    products: list[CartProduct]

def cart_out(cart, db):
    lines = db.query(CartLine).filter(CartLine.cart_id == cart.id).order_by(CartLine.id).all()
    return {'id': cart.id, 'userId': cart.user_id, 'date': cart.date.isoformat(),
            'products': [{'productId': line.product_id, 'quantity': line.quantity} for line in lines]}

def record_cart(db, payload):
    cart = Cart(user_id=payload.userId, date=payload.date)
    db.add(cart)
    db.flush()
    for item in payload.products:
        db.add(CartLine(cart_id=cart.id, product_id=item.productId, quantity=item.quantity))
    db.commit()
    db.refresh(cart)
    return cart

@router.get('')
def list_carts(db: Session = Depends(get_db), reader_id: int = Depends(authorized_reader)):
    return [cart_out(c, db) for c in db.query(Cart).order_by(Cart.date.desc(), Cart.id.desc()).all()]

@router.post('', status_code=201)
def create_cart(payload: CartPayload, db: Session = Depends(get_db)):
    return cart_out(record_cart(db, payload), db)

@router.put('/{cart_id}')
def update_cart(cart_id: int, payload: CartPayload, db: Session = Depends(get_db)):
    # Se conserva un registro histórico de la modificación sin alterar las anteriores.
    return cart_out(record_cart(db, payload), db)

@router.delete('/{cart_id}')
def delete_cart(cart_id: int, payload: CartPayload, db: Session = Depends(get_db)):
    # No se borra el historial: se registra el estado resultante de la operación.
    return cart_out(record_cart(db, payload), db)
