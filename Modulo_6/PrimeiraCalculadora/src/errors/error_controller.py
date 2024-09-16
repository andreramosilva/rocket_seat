from .http_bad_request import HttpBadRequestError
from .http_unprocessable_entity import HttpUnprocessableEntityError

def handle_errors(error: Exception)-> Dict:
    if isinstance(error, HttpUnprocessableEntityError,HttpBadRequestError):
        return {
            "status": error.status_code,
            "body": {"errors" : [{
                "name": error.name,
                "message": error.message
            }]}
        }
    