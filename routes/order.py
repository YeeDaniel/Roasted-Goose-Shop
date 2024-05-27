from flask import request, Blueprint
from services import OrderService

order = Blueprint('order', __name__)

# GET 方法來獲取所有訂單
@order.route('/orders', methods=['GET'])
def get_all_orders():
    orders = OrderService.get_all_orders()
    # 你需要將訂單列表轉換為適合回應的格式，例如 JSON
    return {"orders": [order.to_dict() for order in orders]}

# GET 方法來獲取特定訂單
@order.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = OrderService.get_order_by_id(order_id)
    # 你需要將訂單資訊轉換為適合回應的格式，例如 JSON
    return order.to_dict() if order else {"error": "Order not found"}

# GET 方法來獲取特定使用者的所有訂單
@order.route('/orders/users/<int:user_id>', methods=['GET'])
def get_orders_by_user(user_id):
    orders = OrderService.get_orders_by_user_id(user_id)
    # 你需要將訂單列表轉換為適合回應的格式，例如 JSON
    return {"orders": [order.to_dict() for order in orders]}

# POST 方法來新增訂單
@order.route('/orders', methods=['POST'])
def create_order():
    user_id = request.json.get('user_id')
    total_price = request.json.get('total_price')
    order_time = request.json.get('order_time')
    OrderService.create_order(user_id, total_price, order_time)
    return {"message": "Order created successfully"}

# PUT 方法來更新訂單
@order.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    user_id = request.json.get('user_id')
    total_price = request.json.get('total_price')
    order_time = request.json.get('order_time')
    OrderService.update_order(order_id, user_id, total_price, order_time)
    return {"message": "Order updated successfully"}

# DELETE 方法來刪除訂單
@order.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    OrderService.delete_order(order_id)
    return {"message": "Order deleted successfully"}



