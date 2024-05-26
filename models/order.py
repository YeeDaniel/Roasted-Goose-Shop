from database import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    total_price = db.Column(db.String(80), unique=False, nullable=False)
    order_time = db.Column(db.DateTime, unique=False, nullable=False)

    def __repr__(self):
        return f"Order('{self.product}', '{self.quantity}')"