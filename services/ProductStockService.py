from models.product_stock import Product_stock
from database import db

def update_stock_quantity(product_id, stock_id, new_quantity):
    product_stock = Product_stock.query.filter_by(product_id=product_id, stock_id=stock_id).first()
    if product_stock:
        product_stock.quantity = new_quantity
        db.session.commit()
        return product_stock
    return None


def increment_stock(product_id, stock_id, amount):
    product_stock = Product_stock.query.filter_by(product_id=product_id, stock_id=stock_id).first()
    if product_stock:
        product_stock.quantity += amount
        db.session.commit()
        return product_stock
    return None

def decrement_stock(product_id, stock_id, amount):
    product_stock = Product_stock.query.filter_by(product_id=product_id, stock_id=stock_id).first()
    if product_stock and product_stock.quantity >= amount:
        product_stock.quantity -= amount
        db.session.commit()
        return product_stock
    return None


def get_stock_details(product_id):
    stocks = Product_stock.query.filter_by(product_id=product_id).all()
    return [{'stock_id': stock.stock_id, 'quantity': stock.quantity} for stock in stocks]

def get_quantity(product_id, stock_id):
    product_stock = Product_stock.query.filter_by(product_id=product_id, stock_id=stock_id).first()
    if product_stock:
        return product_stock.quantity
    return None

