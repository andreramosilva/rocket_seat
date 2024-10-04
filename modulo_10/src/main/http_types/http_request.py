class HttpRequest:
    def __init(self, body: dict = None, headers: dict = None, params) -> None:
        self.body = body
        self.headers = headers
        self.params = params