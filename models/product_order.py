from database import db

class Product_order(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)
    
    product = db.relationship('Product', backref='Product_of_product_orders', lazy=True)
    order = db.relationship('Order', backref='Order_of_product_orders', lazy=True)

    def __repr__(self):
        return f"Product_order('{self.product_id}', '{self.order_id}', '{self.quantity}')"