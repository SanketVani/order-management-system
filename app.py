from flask import Flask
from models import db
from routes import api
from config import Config
import os

app = Flask(__name__)

# Load configuration from Config class
app.config.from_object(Config)

# Fallback for DATABASE_URL if not set
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'postgresql://postgres:123789@localhost/order_management'
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

# Register API routes
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)