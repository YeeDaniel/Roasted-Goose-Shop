from models.stock import Stock
from database import db

def get_all_stocks():
    return Stock.query.all()

def get_stock_by_product_id(product_id):
    return Stock.query.filter_by(product_id=product_id).first()

def update_stock(product_id, quantity):
    stock = Stock.query.filter_by(product_id=product_id).first()
    if stock:
        stock.quantity = quantity
        db.session.commit()

