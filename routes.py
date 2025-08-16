from flask import Blueprint, Flask, jsonify, request
from models import db, Order
from config import Config

api = Blueprint('api',__name__)




@api.route('/orders', methods=['POST'])
def create_order():
       data = request.json
       new_order = Order(customer_name=data['customer_name'],
                         item_name=data['item_name'],
                         quantity=data['quantity'])
       db.session.add(new_order)
       db.session.commit()
       return jsonify(new_order.to_dict()), 201

@api.route('/orders', methods=['GET'])
def list_orders():
       orders = Order.query.order_by(Order.created_at.desc()).all()
       return jsonify([order.to_dict() for order in orders]), 200

@api.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
       order = Order.query.get_or_404(order_id)
       return jsonify(order.to_dict()), 200

@api.route('/track/<string:tracking_id>', methods=['GET'])
def track_order(tracking_id):
       order = Order.query.filter_by(tracking_id=tracking_id).first()
       if order:
           return jsonify({'status': order.status, 'last_updated': order.updated_at}), 200
       return jsonify({'error': 'Order not found'}), 404

@api.route('/orders/<int:order_id>/status', methods=['PUT'])
def update_order_status(order_id):
       data = request.json
       order = Order.query.get_or_404(order_id)
       order.status = data['status']
       db.session.commit()
       return jsonify(order.to_dict()), 200


   