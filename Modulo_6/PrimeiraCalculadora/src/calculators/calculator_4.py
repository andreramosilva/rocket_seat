from src.drivers.interfaces.driver_hander_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from flask import request as FlaskRequest

class Calculator4:
    def __init__(self, driver_handler : DriverHandlerInterface):
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        average = self.__calculate_average(input_data)
        return self.__format_response(average)
        
    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Invalid request")
        input_data = body["numbers"]
        return input_data

    def __calculate_average(self, numbers: List[float]) -> float:
        return self.__driver_handler.average(numbers)

    def __format_response(self, average: float) -> Dict:
        return {
            "data":{
                "calculator": 4,
                "result":  average,
                "success": True
            }
            
        }