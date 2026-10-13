from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import products, users

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


@app.get("/", tags=["Estado"])
def root():
    return {
        "mensaje": "API funcionando correctamente",
        "documentacion": "/docs",
    }
