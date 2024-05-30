from database import db

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Stock('{self.id}', '{self.quantity}')"