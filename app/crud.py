import datetime
from sqlalchemy.orm import Session
from app import models
from app import shemas


# Получение всех товаров
async def get_products(db: Session) -> list[models.Product]:
    result = db.query(models.Product).filter(models.Product.time_deleted == None).all()
    return result


# Получение товара по id
async def get_product_id(db: Session, product_id: int) -> models.Product:
    db_product = db.query(models.Product).filter(models.Product.id == product_id,
                                                 models.Product.time_deleted == None).all()
    return db_product


# Добавление нового товара
async def add_product(db: Session, product: shemas.ProductCreate) -> models.Product:
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# Добавление нового типа продукта
async def add_product_type(db: Session,
                           product_type: shemas.ProductTypeCreate) -> models.ProductType:
    db_product_type = models.ProductType(**product_type.dict())
    db.add(db_product_type)
    db.commit()
    db.refresh(db_product_type)
    return db_product_type


# Обновление продукта
async def update_product(db: Session, product_id: int, product: shemas.ProductCreate) -> models.Product:
    db_product = db.query(models.Product).filter_by(id=product_id)
    db_product.update(product.dict(), synchronize_session='fetch')
    db.commit()
    db_product = db.query(models.Product).filter(models.Product.id == product_id).all()
    return db_product


async def delete_product(db: Session, product_id: int) -> models.Product:
    db_product = db.query(models.Product).filter_by(id=product_id).all()
    db_product[0].time_deleted = datetime.datetime.utcnow()
    db.commit()



# Получение всех товаров по типу
async def get_products_type(db: Session, type_id: int) -> models.Product:
    result = db.query(models.Product).filter(models.Product.product_type_id == type_id, models.Product.time_deleted == None).all()
    return result
