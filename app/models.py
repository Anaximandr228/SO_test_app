from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


# Определение полей таблицы Product_type
class ProductType(Base):
    __tablename__ = "product_type"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    time_deleted = Column(DateTime(timezone=True))

    product = relationship("Product", back_populates="type")


# Определение полей таблицы Product
class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    time_deleted = Column(DateTime(timezone=True))
    name = Column(String(100), nullable=False)
    product_type_id = Column(Integer, ForeignKey("product_type.id"))

    type = relationship("ProductType", back_populates="product")
