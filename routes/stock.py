from flask import request, Blueprint, jsonify
from services import StockService

stock = Blueprint('stock', __name__)

@stock.route('/create', methods=['POST'])
def create_stock():
    data = request.get_json()
    quantity = data.get('quantity')
    if quantity is None:
        return jsonify({"error": "Quantity is required"}), 400
    stock, message = StockService.create_stock(quantity)
    if stock:
        return jsonify({"message": message, "stock": {"id": stock.id, "quantity": stock.quantity}}), 201
    else:
        return jsonify({"error": message}), 400
    
@stock.route('/update/<int:stock_id>', methods=['PUT'])
def update_stock(stock_id):
    data = request.get_json()
    quantity = data.get('quantity')
    if quantity is None:
        return jsonify({"error": "Quantity is required"}), 400
    stock, message = StockService.update_stock(stock_id, quantity)
    if stock:
        return jsonify({"message": message, "stock": {"id": stock.id, "quantity": stock.quantity}}), 200
    else:
        return jsonify({"error": message}), 404
    
@stock.route('/delete/<int:stock_id>', methods=['DELETE'])
def delete_stock(stock_id):
    success, message = StockService.delete_stock(stock_id)
    if success:
        return jsonify({"message": message}), 200
    else:
        return jsonify({"error": message}), 404

@stock.route('/details/<int:stock_id>', methods=['GET'])
def get_stock_details(stock_id):
    stock, message = StockService.get_stock(stock_id)
    if stock:
        return jsonify({"stock": {"id": stock.id, "quantity": stock.quantity}, "message": message}), 200
    else:
        return jsonify({"error": message}), 404

@stock.route('/all', methods=['GET'])
def get_all_stocks():
    stocks, message = StockService.get_all_stocks()
    return jsonify({"stocks": [{"id": stock.id, "quantity": stock.quantity} for stock in stocks], "message": message}), 200