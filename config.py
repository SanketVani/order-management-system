import os

class Config:
       SQLALCHEMY_DATABASE_URI = os.environ.get('') or 'postgresql://postgres:123789@localhost/order_management'
       SQLALCHEMY_TRACK_MODIFICATIONS = False
   