from models.product import Product
from database import db

def create_product(name, description, image, price):
    new_product = Product(name=name, description=description, image=image, price=price)
    db.session.add(new_product)
    db.session.commit()

def update_product(product_id, name=None, description=None, image=None, price=None):
    product = Product.query.get(product_id)
    if product:
        if name:
            product.name = name
        if description:
            product.description = description
        if image:
            product.image = image
        if price:
            product.price = price
        db.session.commit()
        return product
    return None

def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return True
    return False

def get_product_details(product_id):
    product = Product.query.get(product_id)
    return product

def get_all_products():
    return Product.query.all()
