from models.order import Order
from database import db

def create_order(user_id, total_price, order_time):
    order = Order(user_id=user_id, total_price=total_price, order_time=order_time)
    db.session.add(order)
    db.session.commit()
    return order

def get_all_orders():
    return Order.query.all()

def get_order_by_id(order_id):
    return Order.query.filter_by(id=order_id).first()

def get_orders_by_user_id(user_id):
    return Order.query.filter_by(user_id=user_id).all()

def update_order(order_id, user_id, total_price, order_time):
    order = Order.query.filter_by(id=order_id).first()
    if order:
        order.user_id = user_id
        order.total_price = total_price
        order.order_time = order_time
        db.session.commit()
    return order

def delete_order(order_id):
    order = Order.query.filter_by(id=order_id).first()
    db.session.delete(order)
    db.session.commit()
    return order