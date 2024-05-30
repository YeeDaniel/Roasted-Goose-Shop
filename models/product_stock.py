from database import db

class Product_stock(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
    stock = db.relationship('Stock', backref='Stock_product_stocks', lazy=True)

    def __repr__(self):
        return f"Product_stock('{self.product_id}', '{self.stock_id}', '{self.quantity}')"