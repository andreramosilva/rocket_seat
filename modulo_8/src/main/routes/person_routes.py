from flask import Blueprint , request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.main.composer.peson_creator_composer import person_creator_composer
from src.main.composer.person_finder_composer import person_finder_composer

person_route_bp = Blueprint('person_routes', __name__)

@person_route_bp.route('/people', methods=['POST'])
def create_person():
    http_request = HttpRequest(body = request.json)
    view = person_creator_composer()

    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status

# TODO: 404 Not Found arrumar rota
@person_route_bp.route('/people', methods=['GET'])
def find_person():
    http_request = HttpRequest()
    view = person_finder_composer()

    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status
