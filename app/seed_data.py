"""
Crea las tablas en MySQL y las llena con datos iniciales.

Uso (desde la carpeta backend_api):
    python -m app.seed_data

Es seguro correrlo varias veces: borra y vuelve a crear los datos
iniciales cada vez (útil para "resetear" la base durante pruebas).
"""
from .database import Base, SessionLocal, engine
from . import models

USERS = [
    dict(id=1, email="john@gmail.com", username="johnd", password="m38rmF$",
         firstname="john", lastname="doe", phone="1-570-236-7033",
         city="kilcoole", street="new road", number=7682, zipcode="12926-3874",
         lat="-37.3159", long="81.1496"),
    dict(id=2, email="morrison@gmail.com", username="mor_2314", password="83r5^_",
         firstname="david", lastname="morrison", phone="1-570-236-7033",
         city="kilcoole", street="Lovers Ln", number=7267, zipcode="12926-3874",
         lat="-37.3159", long="81.1496"),
    dict(id=3, email="kevin@gmail.com", username="kevinryan", password="kev02937@",
         firstname="kevin", lastname="ryan", phone="1-567-094-1345",
         city="Cullman", street="Frances Ct", number=86, zipcode="29567-1452",
         lat="40.3467", long="-30.1310"),
    dict(id=4, email="don@gmail.com", username="donero", password="ewedon",
         firstname="don", lastname="romer", phone="1-765-789-6734",
         city="San Antonio", street="Hunters Creek Dr", number=6454, zipcode="98234-1734",
         lat="50.3467", long="-20.1310"),
    dict(id=5, email="derek@gmail.com", username="derek", password="jklg*_56",
         firstname="derek", lastname="powell", phone="1-956-001-1945",
         city="san Antonio", street="adams St", number=245, zipcode="80796-1234",
         lat="40.3467", long="-40.1310"),
    dict(id=6, email="david_r@gmail.com", username="david_r", password="3478*#54",
         firstname="david", lastname="russell", phone="1-678-345-9856",
         city="el paso", street="prospect st", number=124, zipcode="12346-0456",
         lat="20.1677", long="-10.6789"),
    dict(id=7, email="miriam@gmail.com", username="snyder", password="f238&@*$",
         firstname="miriam", lastname="snyder", phone="1-123-943-0563",
         city="fresno", street="saddle st", number=1342, zipcode="96378-0245",
         lat="10.3456", long="20.6419"),
    dict(id=8, email="william@gmail.com", username="hopkins", password="William56$hj",
         firstname="william", lastname="hopkins", phone="1-478-001-0890",
         city="mesa", street="vally view ln", number=1342, zipcode="96378-0245",
         lat="50.3456", long="10.6419"),
    dict(id=9, email="kate@gmail.com", username="kate_h", password="kfejk@*_",
         firstname="kate", lastname="hale", phone="1-678-456-1934",
         city="miami", street="avondale ave", number=345, zipcode="96378-0245",
         lat="40.12456", long="20.5419"),
    dict(id=10, email="jimmie@gmail.com", username="jimmie_k", password="klein*#%*",
         firstname="jimmie", lastname="klein", phone="1-104-001-4567",
         city="fort wayne", street="oak lawn ave", number=526, zipcode="10256-4532",
         lat="30.24788", long="-20.545419"),
]

# Catálogo de ejemplo: 4 categorías, igual que fakestoreapi.
# Las imágenes usan picsum.photos (servicio público de imágenes de ejemplo).
def _img(n: int) -> str:
    return f"https://picsum.photos/seed/producto{n}/400/400"


PRODUCTS = [
    # --- electronics ---
    dict(title="Disco duro portátil 2TB USB 3.0", price=64.99,
         description="Almacenamiento externo compacto, compatible con PC, Mac y consolas. Velocidad de transferencia de hasta 5 Gbps.",
         category="electronics", image=_img(1)),
    dict(title="SSD interno 1TB SATA III", price=109.0,
         description="Unidad de estado sólido de alto rendimiento para acelerar el arranque y la carga de aplicaciones.",
         category="electronics", image=_img(2)),
    dict(title="Memoria USB 128GB", price=18.5,
         description="Memoria flash compacta con carcasa metálica y conexión USB 3.2.",
         category="electronics", image=_img(3)),
    dict(title="Monitor curvo 27 pulgadas 144Hz", price=399.99,
         description="Panel VA curvo Full HD con tasa de refresco de 144Hz, ideal para gaming y trabajo multitarea.",
         category="electronics", image=_img(4)),
    dict(title="Audífonos inalámbricos con cancelación de ruido", price=129.9,
         description="Bluetooth 5.3, hasta 30 horas de batería y micrófono integrado para llamadas.",
         category="electronics", image=_img(5)),

    # --- jewelery ---
    dict(title="Anillo de plata esterlina con circonia", price=45.0,
         description="Anillo ajustable en plata 925 con piedra central de circonia cúbica.",
         category="jewelery", image=_img(6)),
    dict(title="Collar de oro laminado con dije de corazón", price=78.5,
         description="Cadena de 45 cm con dije de corazón, acabado en oro laminado de 18k.",
         category="jewelery", image=_img(7)),
    dict(title="Pulsera de acero inoxidable", price=32.0,
         description="Pulsera unisex resistente al agua y al desgaste, cierre de seguridad.",
         category="jewelery", image=_img(8)),
    dict(title="Aretes de perla cultivada", price=59.9,
         description="Aretes clásicos con perla de agua dulce y base de plata.",
         category="jewelery", image=_img(9)),

    # --- men's clothing ---
    dict(title="Chamarra impermeable ligera para hombre", price=84.0,
         description="Chamarra cortavientos con capucha plegable y bolsillos con cierre.",
         category="men's clothing", image=_img(10)),
    dict(title="Playera de algodón manga corta", price=15.99,
         description="Playera básica de algodón peinado, corte regular, disponible en varios colores.",
         category="men's clothing", image=_img(11)),
    dict(title="Pantalón de mezclilla slim fit", price=49.5,
         description="Jeans de corte ajustado con elástico para mayor comodidad.",
         category="men's clothing", image=_img(12)),
    dict(title="Sudadera con capucha unisex", price=39.0,
         description="Sudadera de felpa suave con bolsillo canguro y puños acanalados.",
         category="men's clothing", image=_img(13)),

    # --- women's clothing ---
    dict(title="Vestido casual de verano floral", price=42.0,
         description="Vestido ligero de tirantes con estampado floral, ideal para clima cálido.",
         category="women's clothing", image=_img(14)),
    dict(title="Blusa de manga larga con botones", price=27.5,
         description="Blusa de tela fluida con cuello camisero, versátil para oficina o diario.",
         category="women's clothing", image=_img(15)),
    dict(title="Leggings deportivos de cintura alta", price=24.9,
         description="Leggings elásticos y transpirables, con bolsillo lateral para el celular.",
         category="women's clothing", image=_img(16)),
    dict(title="Abrigo largo de lana mezclada", price=119.0,
         description="Abrigo elegante con solapa y cinturón, forro interior suave.",
         category="women's clothing", image=_img(17)),
]


def run():
    # Recrea todas las tablas desde cero.
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        for u in USERS:
            db.add(models.User(**u))
        for p in PRODUCTS:
            db.add(models.Product(**p))
        db.commit()
        print(f"✔ {len(USERS)} usuarios y {len(PRODUCTS)} productos cargados.")
    finally:
        db.close()


if __name__ == "__main__":
    run()
