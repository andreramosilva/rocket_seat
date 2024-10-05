from flask import Blueprint, request, jsonify
from src.main.http_types.http_request import HttpRequest
from src.main.composer.registry_order_composer import registry_order_composer


delivery_routes_bp = Blueprint('delivery_routes', __name__)

@delivery_routes_bp.route('/delivery/order', methods=['POST'])
def registry_order():
    registry_order_use_case = registry_order_composer()
    order = request.json
    http_request = HttpRequest(body=order)

    #enviar o http_request para a nossa logica
    response = registry_order_use_case.registry(http_request)

    #logica ira retornar o http_response


    return jsonify(response.body), response.status_code
