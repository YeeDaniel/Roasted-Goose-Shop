from flask import request, Blueprint, jsonify
from services import ProductService

product = Blueprint('product', __name__)

@product.route('/create', methods=['POST'])
def create_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    image = data.get('image')
    price = data.get('price')
    if not all([name, description, image, price]):
        return {"error": "Missing data"}, 400
    product = ProductService.create_product(name, description, image, price)
    return {"message": "Product created successfully", "product": product.id}, 201

@product.route('/update/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    image = data.get('image')
    price = data.get('price')
    product = ProductService.update_product(product_id, name, description, image, price)
    if product:
        return {"message": "Product updated successfully", "product": product.id}, 200
    else:
        return {"error": "Product not found"}, 404
    
@product.route('/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    success = ProductService.delete_product(product_id)
    if success:
        return {"message": "Product deleted successfully"}, 200
    else:
        return {"error": "Product not found"}, 404
    
@product.route('/details/<int:product_id>', methods=['GET'])
def get_product_details(product_id):
    product = ProductService.get_product_details(product_id)
    if product:
        # 构建一个字典，包含所有需要的产品信息
        product_details = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'image': product.image,
            'price': product.price
        }
        return jsonify(product_details), 200
    else:
        return jsonify({"error": "Product not found"}), 404

@product.route('/all', methods=['GET'])
def get_all_products():
    products = ProductService.get_all_products()
    return {"products": [str(product) for product in products]}, 200