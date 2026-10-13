from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


# ---------- USERS ----------

class GeoLocation(BaseModel):
    lat: str
    long: str


class AddressOut(BaseModel):
    geolocation: GeoLocation
    city: str
    street: str
    number: int
    zipcode: str


class NameOut(BaseModel):
    firstname: str
    lastname: str


class UserOut(BaseModel):
    # Misma estructura anidada que devuelve fakestoreapi.com/users
    address: AddressOut
    id: int
    email: str
    username: str
    password: str
    name: NameOut
    phone: str
    v: int = Field(default=0, serialization_alias="__v")

    model_config = ConfigDict(populate_by_name=True)


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    token: str


# ---------- PRODUCTS ----------

class ProductBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    price: float = Field(..., gt=0)
    description: str = Field(..., min_length=1)
    category: str = Field(..., min_length=1, max_length=80)
    # Validación de formato de URL (US06: "URL con formato correcto")
    image: HttpUrl


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductOut(BaseModel):
    id: int
    title: str
    price: float
    description: str
    category: str
    image: str

    model_config = ConfigDict(from_attributes=True)
