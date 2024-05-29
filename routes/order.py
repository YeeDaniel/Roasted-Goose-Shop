from dateutil import parser
from flask import request, Blueprint, jsonify
from services import OrderService

order = Blueprint('order', __name__)

@order.route('/create/', methods=['POST'])
def create_order():
    data = request.get_json()
    user_id = data.get('user_id')
    total_price = data.get('total_price')
    order_time_str = data.get('order_time')

    if not all([user_id, total_price, order_time_str]):
        return jsonify({"error": "Missing data"}), 400

    try:
        order_time = parser.parse(order_time_str)
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400

    # 假设已经有了一个 OrderService.create_order 方法处理业务逻辑
    order, message = OrderService.create_order(user_id, total_price, order_time)
    if order:
        return jsonify({"message": message, "order": order.id}), 201
    else:
        return jsonify({"error": message}), 40

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