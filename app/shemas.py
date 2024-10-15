from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ProductTypeBase(BaseModel):
    name: str


class ProductTypeCreate(ProductTypeBase):
    name: str


class ProductType(ProductTypeBase):
    id: int
    time_created: datetime
    time_updated: Optional[datetime]
    name: str

    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    name: str


class ProductCreate(ProductBase):
    name: str
    product_type_id: int


class Product(ProductBase):
    id: int
    time_created: datetime
    time_updated: Optional[datetime]
    name: str
    product_type_id: int
    type: ProductType

    class Config:
        from_attributes = True
