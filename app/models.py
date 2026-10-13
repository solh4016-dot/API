from sqlalchemy import Column, Float, Integer, String, Text

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(120), nullable=False)
    username = Column(String(60), nullable=False, unique=True, index=True)
    password = Column(String(120), nullable=False)
    firstname = Column(String(60), nullable=False)
    lastname = Column(String(60), nullable=False)
    phone = Column(String(30), nullable=False)

    # Dirección (se guarda aplanada y se reconstruye anidada en la respuesta
    # para que el JSON tenga la misma forma que fakestoreapi.com/users)
    city = Column(String(80), nullable=False)
    street = Column(String(120), nullable=False)
    number = Column(Integer, nullable=False)
    zipcode = Column(String(20), nullable=False)
    lat = Column(String(20), nullable=False)
    long = Column(String(20), nullable=False)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(80), nullable=False, index=True)
    image = Column(String(500), nullable=False)
