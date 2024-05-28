from flask import request, Blueprint
from services import OrderService

order = Blueprint('order', __name__)

def create_order():
    data = request.get_json()
    user_id = data.get('user_id')
    total_price = data.get('total_price')
    order_time = data.get('order_time')

    if not all([user_id, total_price, order_time]):
        return {"error": "Missing data"}, 400

    order, message = OrderService.create_order(user_id, total_price, order_time)
    if order:
        return {"message": message, "order": order.id}, 201
    else:
        return {"error": message}, 400

@order.route('/update/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.get_json()
    total_price = data.get('total_price')
    order_time = data.get('order_time')

    order, message = OrderService.update_order(order_id, total_price, order_time)
    if order:
        return {"message": message, "order": order.id}, 200
    else:
        return {"error": message}, 404

@order.route('/delete/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    success, message = OrderService.delete_order(order_id)
    if success:
        return {"message": message}, 200
    else:
        return {"error": message}, 404

@order.route('/details/<int:order_id>', methods=['GET'])
def get_order_details(order_id):
    order, message = OrderService.get_order(order_id)
    if order:
        return {"order": order, "message": message}, 200
    else:
        return {"error": message}, 404

@order.route('/all', methods=['GET'])
def get_all_orders():
    orders, message = OrderService.get_all_orders()
    return {"orders": orders, "message": message}, 200