"""US09/US10: endpoints de práctica; no guardan carritos en MySQL.
La aplicación mantiene el estado del carrito en su dispositivo.
"""
from datetime import datetime
from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix='/carts', tags=['Carritos (US09/US10)'])


class CartProduct(BaseModel):
    productId: int = Field(gt=0)
    quantity: int = Field(gt=0)


class CartPayload(BaseModel):
    userId: int = Field(gt=0)
    date: datetime
    products: list[CartProduct]


@router.post('', status_code=201)
def create_cart(payload: CartPayload):
    """Confirma POST sin persistencia remota (simulación Fake Store)."""
    return {'id': payload.userId, **payload.model_dump(mode='json')}


@router.put('/{cart_id}')
def update_cart(cart_id: int, payload: CartPayload):
    """Confirma cambios de cantidad; el cálculo vive en Flutter."""
    return {'id': cart_id, **payload.model_dump(mode='json')}


@router.delete('/{cart_id}')
def delete_cart(cart_id: int, payload: CartPayload):
    """Confirma eliminación de artículos en el estado local de Flutter."""
    return {'id': cart_id, **payload.model_dump(mode='json')}
