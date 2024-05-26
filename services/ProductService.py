from models.product import Product
from database import db

# add_product
def add_product(name, description, price):
    new_product = Product(name=name, description=description, price=price)
    db.session.add(new_product)
    db.session.commit()

# get_all_products
def get_all_products():
    return Product.query.all()

# get_product_by_id
def get_product_by_id(product_id):
    return Product.query.filter_by(id=product_id).first()

# update_product
def update_product(product_id, name, description, price):
    product = Product.query.get(product_id)
    if product:
        product.name = name
        product.description = description
        product.price = price
        db.session.commit()

# delete_product
def delete_product(product_id):
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()