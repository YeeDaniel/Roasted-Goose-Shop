from database import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    order_time = db.Column(db.DateTime, nullable=False)

    product_orders = db.relationship('Product_order', back_populates='order', lazy=True, overlaps="product_orders")

    def __repr__(self):
        return f"Order('{self.id}', '{self.total_price}')"