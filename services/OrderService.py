from models.order import Order
from database import db

def create_order(user_id, total_price, order_time):
    if total_price < 0:
        return None, "Total price cannot be negative"
    new_order = Order(user_id=user_id, total_price=total_price, order_time=order_time)
    db.session.add(new_order)
    db.session.commit()
    return new_order, "Order created successfully"


def update_order(order_id, total_price=None, order_time=None):
    order = Order.query.get(order_id)
    if order:
        if total_price is not None < 0:
            return None, "Total price cannot be negative"
        order.total_price = total_price
        order.order_time = order_time
        db.session.commit()
        return order, "Order updated successfully"
    return None, "Order not found"


def delete_order(order_id):
    order = Order.query.get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
        return True, "Order deleted successfully"
    return False, "Order not found"


def get_order(order_id):
    order = Order.query.get(order_id)
    if order:
        return order, "Order found"
    return None, "Order not found"


def get_all_orders():
    orders = Order.query.all()
    return orders, "All orders retrieved"