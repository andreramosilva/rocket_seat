from typing import Dict, List

class HttpResponse:
    def __init__(self, status: int, body: Dict = None) -> None:
        self.status = status
        self.body = body

    def get_status(self) -> int:
        return self.status

    def get_body(self) -> Dict:
        return self.body