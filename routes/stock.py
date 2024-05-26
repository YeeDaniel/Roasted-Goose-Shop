from flask import request, Blueprint
from services import StockService

stock = Blueprint('stock', __name__)

# GET 方法來獲取所有庫存
@stock.route('/stocks', methods=['GET'])
def get_all_stocks():
    stocks = StockService.get_all_stocks()
    # 你需要將庫存列表轉換為適合回應的格式，例如 JSON
    return {"stocks": [stock.to_dict() for stock in stocks]}

# GET 方法來獲取特定庫存
@stock.route('/stocks/<int:product_id>', methods=['GET'])
def get_stock(product_id):
    stock = StockService.get_stock_by_product_id(product_id)
    # 你需要將庫存資訊轉換為適合回應的格式，例如 JSON
    return stock.to_dict() if stock else {"error": "Stock not found"}

# PUT 方法來更新庫存
@stock.route('/stocks/<int:product_id>', methods=['PUT'])
def update_stock(product_id):
    quantity = request.json.get('quantity')
    StockService.update_stock(product_id, -quantity)
    return {"message": "Stock updated successfully"}