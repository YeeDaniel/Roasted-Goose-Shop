from database import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey('Stock.id'), nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(80), unique=False, nullable=False)
    image = db.Column(db.String(80), unique=False, nullable=False)
    price = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f"Product('{self.name}', '{self.price}', '{self.stock}')"