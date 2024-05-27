from flask import request, Blueprint, jsonify
from services import ProductOrderService

product_order = Blueprint('product_order', __name__)

# GET 方法來獲取所有訂單
@product_order.route('/product_orders', methods=['GET'])
def get_all_product_orders():
    product_orders = ProductOrderService.get_all_product_orders()
    # 你需要將訂單列表轉換為適合回應的格式，例如 JSON
    return jsonify({"product_orders": [product_order.to_dict() for product_order in product_orders]})

# GET 方法來獲取特定訂單
@product_order.route('/product_orders/<int:product_order_id>', methods=['GET'])
def get_product_order(product_order_id):
    product_order = ProductOrderService.get_product_order_by_id(product_order_id)
    # 你需要將訂單資訊轉換為適合回應的格式，例如 JSON
    return jsonify(product_order.to_dict()) if product_order else {"error": "Product Order not found"}

# GET 方法來獲取特定訂單的所有商品
@product_order.route('/product_orders/orders/<int:order_id>', methods=['GET'])
def get_product_orders_by_order(order_id):
    product_orders = ProductOrderService.get_product_orders_by_order_id(order_id)
    # 你需要將訂單列表轉換為適合回應的格式，例如 JSON
    return jsonify({"product_orders": [product_order.to_dict() for product_order in product_orders]})

# POST 方法來新增訂單
@product_order.route('/product_orders', methods=['POST'])
def create_product_order():
    order_id = request.json.get('order_id')
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity')
    ProductOrderService.create_product_order(order_id, product_id, quantity)
    return jsonify({"message": "Product Order created successfully"})

# PUT 方法來更新訂單
@product_order.route('/product_orders/<int:product_order_id>', methods=['PUT'])
def update_product_order(product_order_id):
    quantity = request.json.get('quantity')
    ProductOrderService.update_product_order(product_order_id, quantity)
    return jsonify({"message": "Product Order updated successfully"})

# DELETE 方法來刪除訂單
@product_order.route('/product_orders/<int:product_order_id>', methods=['DELETE'])
def delete_product_order(product_order_id):
    ProductOrderService.delete_product_order(product_order_id)
    return jsonify({"message": "Product Order deleted successfully"})