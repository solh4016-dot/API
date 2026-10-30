from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db
from ..security import create_token, decode_token
from ..dependencies import authorized_reader
from fastapi import Header

router = APIRouter(tags=["Usuarios y autenticación"])


def _user_to_out(u: models.User) -> dict:
    """Convierte la fila plana de MySQL al JSON anidado estilo fakestoreapi."""
    return {
        "address": {
            "geolocation": {"lat": u.lat, "long": u.long},
            "city": u.city,
            "street": u.street,
            "number": u.number,
            "zipcode": u.zipcode,
        },
        "id": u.id,
        "email": u.email,
        "username": u.username,
        "name": {"firstname": u.firstname, "lastname": u.lastname},
        "phone": u.phone,
        "__v": 0,
    }


# Lista de usuarios -> GET /users
# (la app de Flutter usa este endpoint para validar credenciales)
@router.get("/users")
def list_users(db: Session = Depends(get_db), reader_id: int = Depends(authorized_reader)):
    users = db.query(models.User).order_by(models.User.id).all()
    return [_user_to_out(u) for u in users]


# US01 - Escenario 1 y 2: POST /auth/login
# 200 + token si las credenciales son válidas, 401 si no.
@router.post("/auth/login", response_model=schemas.LoginResponse)
def login(payload: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = (
        db.query(models.User)
        .filter(
            models.User.username == payload.username,
            models.User.password == payload.password,
        )
        .first()
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña inválidos",
        )

    # JWT firmado con el id del usuario en "sub" (como fakestoreapi.com):
    # la app puede decodificarlo para mapear el rol (US01 - Escenario 1).
    return {"token": create_token(user.id, user.username)}


@router.get('/auth/me')
def authenticated_profile(authorization: str | None = Header(default=None), db: Session = Depends(get_db)):
    if not authorization or not authorization.startswith('Bearer '):
        raise HTTPException(status_code=401, detail='Falta token')
    try:
        user_id = int(decode_token(authorization[7:])['sub'])
    except (ValueError, TypeError, KeyError):
        raise HTTPException(status_code=401, detail='Token inválido o expirado')
    user = db.get(models.User, user_id)
    if user is None:
        raise HTTPException(status_code=401, detail='Usuario inexistente')
    return _user_to_out(user)
