from database import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(80), nullable=False)
    price = db.Column(db.String(80), nullable=False)
    stocks = db.relationship('Product_stock', backref='ProductStock_product', lazy=True)

    def __repr__(self):
        return f"Product('{self.name}', '{self.price}')"