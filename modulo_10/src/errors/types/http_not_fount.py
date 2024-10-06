
class HttpUnprocessableEntityError(HttpError):
    def __init__(self, message: str = "Unprocessable Entity", code: int = 422, data: dict = None):
        super().__init__(message, code, data)