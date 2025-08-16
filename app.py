from flask import Flask
from models import db
from routes import api
import os
from config import Config



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('postgresql://postgres:123789@localhost/order_management')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)