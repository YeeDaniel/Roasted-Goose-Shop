from database import db

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('Product.id'), nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f"Stock('{self.location}', '{self.stock}')"