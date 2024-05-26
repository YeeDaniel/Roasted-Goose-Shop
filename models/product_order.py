from database import db

class Product_order(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('Product.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('Order.id'), nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f"product_order('{self.product}', '{self.quantity}')"