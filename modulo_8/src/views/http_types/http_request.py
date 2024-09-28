from typing import Dict, List

class HttpRequest:
    def __init__(self, body: Dict = None, param: Dict = None) -> None:
        self.body = body
        self.param = param


    def get_body(self) -> Dict:
        return self.body

    def get_param(self) -> Dict:
        return self.param
