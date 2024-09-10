from typing import Dict
from flask import request as FlaskRequest


class Calculator1:
    ''''
    * um primeiro numero é dividido em 3 partes iguais

    * a primeira parte é dividida por 4 e seu resultado somado a 7,
    após isso, o resultado é elevado ao quadrado e multiplicado por 0.257

    * segunda parte é elevada a 2.121, dividida por 5 e somado a 1

    * a terceira parte se mantem o mesmo valor
    '''

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        splited_numer = input_data / 3
        primeira_parte = self.__first_process(splited_numer)
        segunda_parte = self.__second_process(splited_numer)
        calculo_final = primeira_parte + segunda_parte + splited_numer

        return self.__format_response(calculo_final)


    def __validate_body(self, body: Dict) -> float:
        if 'number' not in body :
            raise Exception('Body mal formatado')
        input_data = body["number"]
        return input_data
    
    def __first_process(self,first_number : float) -> float:
        result = first_number / 4
        result += 7
        result = result ** 2
        result *= 0.257
        return result
    
    def __second_process(self,second_number : float) -> float:
        result = second_number ** 2.121
        result /= 5
        result += 1
        return result
    
    def __format_response(self, result: float) -> Dict:
        return {
            "data":{
                "calculator": 1,
                "result": round(result,2)
            }
            
        }