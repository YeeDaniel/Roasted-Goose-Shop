from database import db
from models.stock import Stock
    
def create_stock(quantity):
    if quantity < 0:
        return None, "Quantity cannot be negative"
    new_stock = Stock(quantity=quantity)
    db.session.add(new_stock)
    db.session.commit()
    return new_stock, "Stock created successfully"


def update_stock(stock_id, quantity):
    stock = Stock.query.get(stock_id)
    if stock:
        if quantity < 0:
            return None, "Quantity cannot be negative"
        stock.quantity = quantity
        db.session.commit()
        return stock, "Stock updated successfully"
    return None, "Stock not found"


def delete_stock(stock_id):
    stock = Stock.query.get(stock_id)
    if stock:
        db.session.delete(stock)
        db.session.commit()
        return True, "Stock deleted successfully"
    return False, "Stock not found"


def get_stock(stock_id):
    stock = Stock.query.get(stock_id)
    if stock:
        return stock, "Stock found"
    return None, "Stock not found"


def get_all_stocks():
    return Stock.query.all(), "All stocks retrieved"