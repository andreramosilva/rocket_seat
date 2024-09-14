from src.calculators.calculator_2 import Calculator2
from typing import Dict
from src.drivers.numpy_handler import NumpyHandler

class MockRequest:
    def __init__(self, body: Dict)->None    :
        self.json = body

def test_calculate():
    mock_request = MockRequest({"numbers": [1, 2, 3]})

    driver = NumpyHandler()
    calculator = Calculator2(driver)
    result = calculator.calculate(mock_request)
    
    assert isinstance(result, dict)
    assert result == { "data": { "calculator": 2, "result": 0.14 }}
    
    