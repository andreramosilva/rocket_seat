from flask import Blueprint, request, jsonify
from src.main.http_types.http_request import HttpRequest

delivery_routes_bp = Blueprint('delivery_routes', __name__)

@delivery_routes_bp.route('/delivery/order', methods=['POST'])
def registry_order():
    order = request.json
    http_request = HttpRequest(body=order)

    #enviar o http_request para a nossa logica

    #logica ira retornar o http_response

    
    return jsonify(order), 201