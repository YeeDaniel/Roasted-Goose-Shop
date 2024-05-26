from database import db
from sqlalchemy.orm import relationship

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('Product.id'), nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)

    product = relationship('Product', backref='stock', uselist=False)

    def __repr__(self):
        return f"Stock('{self.product.name}', '{self.quantity}')"