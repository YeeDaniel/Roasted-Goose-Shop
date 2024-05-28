from database import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_price = db.Column(db.Float, unique=False, nullable=False)
    order_time = db.Column(db.DateTime, unique=False, nullable=False)

    product_orders = db.relationship('Product_order', backref='Product_order_order', lazy=True)

    def __repr__(self):
        return f"Order('{self.id}', '{self.total_price}')"