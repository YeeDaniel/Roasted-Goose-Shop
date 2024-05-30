from models.product_order import Product_order
from database import db

def create_product_order(product_id, order_id, quantity):
    if quantity <= 0:
        return None, "Quantity must be positive"
    new_product_order = Product_order(product_id=product_id, order_id=order_id, quantity=quantity)
    db.session.add(new_product_order)
    db.session.commit()
    return new_product_order, "Product order created successfully"


def update_product_order(product_order_id, quantity):
    product_order = Product_order.query.get(product_order_id)
    if product_order:
        if quantity <= 0:
            return None, "Quantity must be positive"
        product_order.quantity = quantity
        db.session.commit()
        return product_order, "Product order updated successfully"
    return None, "Product order not found"


def delete_product_order(product_order_id):
    product_order = Product_order.query.get(product_order_id)
    if product_order:
        db.session.delete(product_order)
        db.session.commit()
        return True, "Product order deleted successfully"
    return False, "Product order not found"


def get_product_order(product_order_id):
    product_order = Product_order.query.get(product_order_id)
    if product_order:
        return product_order, "Product order found"
    return None, "Product order not found"


def get_all_product_orders():
    product_orders = Product_order.query.all()
    return product_orders, "All product orders retrieved"