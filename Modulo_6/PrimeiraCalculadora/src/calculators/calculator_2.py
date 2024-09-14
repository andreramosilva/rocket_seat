from flask import  request as FlaskRequest
from typing import Dict, List
from src.drivers.interfaces.driver_hander_interface import DriverHandlerInterface

class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        print(body)
        input_data = self.__validate_body(body)
        calculated_numer = self.__process_data(input_data)
        formated_response = self.__format_response(calculated_numer)
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("Invalid request")
        input_data = body["numbers"]
        return input_data
    
    def __process_data(self, input_data: List[float]) -> float:
        first_process = [(num * 11) ** 0.95 for num in input_data]
        
        result = self.__driver_handler.standard_deviation(first_process)
        
        return 1/result
        
    def __format_response(self, calculated_number: float) -> Dict:
        return {
            "data":{
                "calculator": 2,
                "result": round(calculated_number,2)
            }
            
        }