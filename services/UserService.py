from models.user import User
from database import db

def register(username, email, password):
    user = User.query.filter_by(email=email).first()
    if user:
        return False

    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def login(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return user
    return None
