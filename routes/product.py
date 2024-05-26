from flask import request, Blueprint
from services import ProductService

product = Blueprint('product', __name__)

# GET 方法來獲取所有產品
@product.route('/products', methods=['GET'])
def get_all_products():
    products = ProductService.get_all_products()
    # 你需要將產品列表轉換為適合回應的格式，例如 JSON
    return {"products": [product.to_dict() for product in products]}

# GET 方法來獲取特定產品
@product.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = ProductService.get_product_by_id(product_id)
    # 你需要將產品資訊轉換為適合回應的格式，例如 JSON
    return product.to_dict() if product else {"error": "Product not found"}

# POST 方法來新增產品
@product.route('/products', methods=['POST'])
def add_product():
    name = request.json.get('name')
    description = request.json.get('description')
    price = request.json.get('price')
    ProductService.add_product(name, description, price)
    return {"message": "Product added successfully"}

# PUT 方法來更新產品
@product.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    name = request.json.get('name')
    description = request.json.get('description')
    price = request.json.get('price')
    ProductService.update_product(product_id, name, description, price)
    return {"message": "Product updated successfully"}

# DELETE 方法來刪除產品
@product.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    ProductService.delete_product(product_id)
    return {"message": "Product deleted successfully"}