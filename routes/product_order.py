from flask import request, Blueprint, jsonify
from services import ProductOrderService

product_order = Blueprint('product_order', __name__)

@product_order.route('/create', methods=['POST'])
def create_product_order():
    data = request.get_json()
    product_id = data.get('product_id')
    order_id = data.get('order_id')
    quantity = data.get('quantity')

    if not all([product_id, order_id, quantity]):
        return jsonify({"error": "Missing data"}), 400

    product_order, message = ProductOrderService.create_product_order(product_id, order_id, quantity)
    if product_order:
        return jsonify({"message": message, "product_order": product_order.id}), 201
    else:
        return jsonify({"error": message}), 400

@product_order.route('/update/<int:product_order_id>', methods=['PUT'])
def update_product_order(product_order_id):
    data = request.get_json()
    quantity = data.get('quantity')

    if quantity is None:
        return jsonify({"error": "Quantity is required"}), 400

    product_order, message = ProductOrderService.update_product_order(product_order_id, quantity)
    if product_order:
        return jsonify({"message": message, "product_order": product_order.id}), 200
    else:
        return jsonify({"error": message}), 404

@product_order.route('/delete/<int:product_order_id>', methods=['DELETE'])
def delete_product_order(product_order_id):
    success, message = ProductOrderService.delete_product_order(product_order_id)
    if success:
        return jsonify({"message": message}), 200
    else:
        return jsonify({"error": message}), 404

@product_order.route('/details/<int:product_order_id>', methods=['GET'])
def get_product_order_details(product_order_id):
    product_order, message = ProductOrderService.get_product_order(product_order_id)
    if product_order:
        return jsonify({"product_order": product_order, "message": message}), 200
    else:
        return jsonify({"error": message}), 404

@product_order.route('/all', methods=['GET'])
def get_all_product_orders():
    product_orders, message = ProductOrderService.get_all_product_orders()
    return jsonify({"product_orders": product_orders, "message": message}), 200