from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..models import models
from ..views import schemas
from ..database import get_db

router = APIRouter(prefix="/products", tags=["Productos"])


# US03 - Catálogo general -> GET /products
@router.get("", response_model=List[schemas.ProductOut])
def list_products(db: Session = Depends(get_db)):
    return db.query(models.Product).order_by(models.Product.id).all()


# US04 - Escenario 1: categorías disponibles -> GET /products/categories
# IMPORTANTE: esta ruta debe declararse ANTES de "/{product_id}", si no
# FastAPI intentaría interpretar la palabra "categories" como un id.
@router.get("/categories", response_model=List[str])
def list_categories(db: Session = Depends(get_db)):
    rows = (
        db.query(models.Product.category)
        .distinct()
        .order_by(models.Product.category)
        .all()
    )
    return [r[0] for r in rows]


# US04 - Escenario 2: filtrar por categoría -> GET /products/category/{category}
@router.get("/category/{category}", response_model=List[schemas.ProductOut])
def list_by_category(category: str, db: Session = Depends(get_db)):
    return (
        db.query(models.Product)
        .filter(models.Product.category == category)
        .order_by(models.Product.id)
        .all()
    )


# US05 - Detalle de producto -> GET /products/{id}
# Si no existe devuelve 404 (US05 - Escenario 3: "Producto no disponible").
@router.get("/{product_id}", response_model=schemas.ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no disponible",
        )
    return product


# US06 - Crear producto -> POST /products
# A diferencia de fakestoreapi, aquí SÍ se guarda de verdad en MySQL,
# así que el nuevo producto aparecerá después en GET /products.
@router.post("", response_model=schemas.ProductOut, status_code=status.HTTP_201_CREATED)
def create_product(payload: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = models.Product(
        title=payload.title.strip(),
        price=payload.price,
        description=payload.description.strip(),
        category=payload.category.strip(),
        image=str(payload.image),
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


# US07 - Editar producto -> PUT /products/{id}
@router.put("/{product_id}", response_model=schemas.ProductOut)
def update_product(
    product_id: int,
    payload: schemas.ProductUpdate,
    db: Session = Depends(get_db),
):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no disponible",
        )

    product.title = payload.title.strip()
    product.price = payload.price
    product.description = payload.description.strip()
    product.category = payload.category.strip()
    product.image = str(payload.image)

    db.commit()
    db.refresh(product)
    return product


# US08 - Eliminar producto -> DELETE /products/{id}
# Devuelve el objeto eliminado (igual que fakestoreapi). Aquí SÍ se borra
# de verdad: no volverá a aparecer en futuros GET.
@router.delete("/{product_id}", response_model=schemas.ProductOut)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no disponible",
        )

    deleted = schemas.ProductOut.model_validate(product)
    db.delete(product)
    db.commit()
    return deleted
