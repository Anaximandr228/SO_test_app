from pydantic import BaseModel


class ProductTypeBase(BaseModel):
    name: str


class ProductTypeCreate(ProductTypeBase):
    name: str


class ProductType(ProductTypeBase):
    id: int
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
    name: str
    product_type_id: int
    type: ProductType

    class Config:
        from_attributes = True
