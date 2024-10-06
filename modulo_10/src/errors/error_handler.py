from src.main.http_types.htt_response import HttpResponse
from .types.http_not_fount import HttpNotFound
from .types.http_unprocessable_entity import HttpUnprocessableEntity

def error_handler(e: Exception) -> HttpResponse:
    if isinstance(e, HttpNotFound):
        return HttpResponse(
            body = {
                "error": str(e)
            },
            status_code=404)
    if isinstance(e, HttpUnprocessableEntity):
        return HttpResponse(
            body = {
                "error": str(e)
            },
            status_code=422)
    return HttpResponse(
        body = {
            "error": str(e)
        },
        status_code=500)