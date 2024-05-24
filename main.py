from flask import Flask
from routes import default, user, google
from config import Config
from database import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

app.register_blueprint(default)
app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(google, url_prefix="/google")

if __name__ == "__main__":
    app.run(debug=True, port=6018, use_reloader=True)
