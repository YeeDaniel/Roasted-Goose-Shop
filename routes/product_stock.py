from flask import request, Blueprint, jsonify
from services import ProductStockService

product_stock = Blueprint('product_stock', __name__)

@product_stock.route('/update_stock/<int:product_id>/<int:stock_id>', methods=['POST'])
def update_stock(product_id, stock_id):
    data = request.get_json()
    new_quantity = data.get('new_quantity')
    if new_quantity is None:
        return jsonify({'error': 'New quantity is required'}), 400
    result = ProductStockService.update_stock_quantity(product_id, stock_id, new_quantity)
    if result:
        return jsonify({'message': 'Stock updated successfully', 'product_stock': str(result)}), 200
    else:
        return jsonify({'error': 'Product stock not found'}), 404

@product_stock.route('/increment_stock/<int:product_id>/<int:stock_id>', methods=['POST'])
def increment_stock(product_id, stock_id):
    data = request.get_json()
    amount = data.get('amount')
    if amount is None:
        return jsonify({'error': 'Amount is required'}), 400
    result = ProductStockService.increment_stock(product_id, stock_id, amount)
    if result:
        return jsonify({'message': 'Stock incremented successfully', 'product_stock': str(result)}), 200
    else:
        return jsonify({'error': 'Product stock not found'}), 404
    
@product_stock.route('/decrement_stock/<int:product_id>/<int:stock_id>', methods=['POST'])
def decrement_stock(product_id, stock_id):
    data = request.get_json()
    amount = data.get('amount')
    if amount is None:
        return jsonify({'error': 'Amount is required'}), 400
    result = ProductStockService.decrement_stock(product_id, stock_id, amount)
    if result:
        return jsonify({'message': 'Stock decremented successfully', 'product_stock': str(result)}), 200
    else:
        return jsonify({'error': 'Insufficient stock or stock not found'}), 404
    
@product_stock.route('/stock_details/<int:product_id>', methods=['GET'])
def stock_details(product_id):
    results = ProductStockService.get_stock_details(product_id)
    return jsonify({'stock_details': results}), 200

#get quantity
@product_stock.route('/quantity/<int:product_id>/<int:stock_id>', methods=['GET'])
def get_quantity(product_id, stock_id):
    print('product_id', product_id)
    print('stock_id', stock_id)
    result = ProductStockService.get_quantity(product_id, stock_id)
    if result is not None:
        return jsonify({'quantity': result}), 200
    else:
        return jsonify({'error': 'Product stock not found'}), 404