from src.drivers.interfaces.driver_hander_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from flask import request as FlaskRequest
from typing import Dict, List

class Calculator3:
    def __init__(self , driver_handler : DriverHandlerInterface):
        self.__driver_handler = driver_handler
        
    def calculate(self,request : FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_result(variance, multiplication)
        formated_response = self.__format_response(variance)
        return formated_response
    
    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Invalid request")
        input_data = body["numbers"]
        return input_data
    
    def __calculate_variance(self, numbers: List[float]) -> float:
        return self.__driver_handler.variance(numbers)
    
    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1
        for num in numbers:
            multiplication *= num
        return multiplication
    
    def __verify_result(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise Exception("Variance is lower than multiplication")

    def __format_response(self, variance: float) -> Dict:
        return {
            "data":{
                "calculator": 3,
                "result":  variance,
                "success": True
            }
            
        }