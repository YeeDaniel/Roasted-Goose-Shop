from models.product_order import Product_order
from database import db

def create_product_order(order_id, product_id, quantity):
    product_order = Product_order(order_id=order_id, product_id=product_id, quantity=quantity)
    db.session.add(product_order)
    db.session.commit()
    return product_order

def get_product_order_by_id(product_order_id):
    return Product_order.query.filter_by(id=product_order_id).first()

def get_product_orders_by_order_id(order_id):
    return Product_order.query.filter_by(order_id=order_id).all()

def add_product_to_order(order_id, product_id, quantity):
    product_order = Product_order(order_id=order_id, product_id=product_id, quantity=quantity)
    db.session.add(product_order)
    db.session.commit()
    return product_order

def update_product_order(product_order_id, quantity):
    product_order = Product_order.query.filter_by(id=product_order_id).first()
    if product_order:
        product_order.quantity = quantity
        db.session.commit()
    return product_order

def delete_product_order(product_order_id):
    product_order = Product_order.query.filter_by(id=product_order_id).first()
    db.session.delete(product_order)
    db.session.commit()
    return product_order