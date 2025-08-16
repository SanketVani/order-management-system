from flask_sqlalchemy import SQLAlchemy  
from datetime import datetime
import uuid

db = SQLAlchemy()

class Order(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       customer_name = db.Column(db.String(100), nullable=False)
       item_name = db.Column(db.String(100), nullable=False)
       quantity = db.Column(db.Integer, nullable=False)
       tracking_id = db.Column(db.String(36), unique=True, default=lambda: str(uuid.uuid4()))
       status = db.Column(db.String(20), default='PENDING')
       created_at = db.Column(db.DateTime, default=datetime.utcnow)
       updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

       def to_dict(self):
           return {
               'id': self.id,
               'customer_name': self.customer_name,
               'item_name': self.item_name,
               'quantity': self.quantity,
               'tracking_id': self.tracking_id,
               'status': self.status,
               'created_at': self.created_at,
               'updated_at': self.updated_at
           }
   