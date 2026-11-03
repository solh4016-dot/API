from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .controllers import products, users, carts

app = FastAPI(
    title="Fake Store API (clon local)",
    description=(
        "API propia en FastAPI + MySQL que replica los endpoints de "
        "fakestoreapi.com usados en la app móvil (US01 a US08)."
    ),
    version="1.0.0",
)

# CORS: permite que la app de Flutter corriendo en Chrome (web) pueda
# llamar a esta API. Sin esto, el navegador bloquearía las peticiones.
# Para producción conviene limitar "allow_origins" a dominios concretos.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(products.router)
app.include_router(carts.router)


@app.get("/", tags=["Estado"])
def root():
    return {
        "mensaje": "API funcionando correctamente",
        "documentacion": "/docs",
    }


@app.get("/health", tags=["Estado"])
def health():
    """Comprueba que FastAPI está activo sin depender de MySQL."""
    return {"status": "ok", "service": "fastapi"}


@app.get("/health/db", tags=["Estado"])
def health_database():
    """Comprueba la conexión real a MySQL, sin exponer credenciales."""
    from fastapi import HTTPException
    from sqlalchemy import text
    from sqlalchemy.exc import SQLAlchemyError
    from .database import engine

    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except SQLAlchemyError:
        raise HTTPException(status_code=503, detail="No se puede conectar con MySQL; revisa la configuración en Render")
