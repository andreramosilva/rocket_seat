from flask import Blueprint, jsonify

pet_route_bp = Blueprint('pets_routes', __name__)

@pet_route_bp.route('/pets', methods=['GET'])
def get_pets():
    return jsonify({'message': 'Hello, World!'})
