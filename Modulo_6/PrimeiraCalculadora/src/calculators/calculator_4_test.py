from src.drivers.numpy_handler import NumpyHandler
from .calculator_4 import Calculator4
from typing import Dict , List
from pytest import raises

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler():
    def average(self, data: List[float])->float:
        return 55.0
    
def test_calculate():
    mock_request = MockRequest({"numbers":[1,1,1,1,100]})
    calculator = Calculator4(MockDriverHandler())
    calc = calculator.calculate(mock_request)
    assert calc == {"data": {"calculator": 4, "result": 55.0, "success": True}}

def test_calculate_with_error():
    mock_request = MockRequest({})
    calculator = Calculator4(MockDriverHandler())
    with raises(Exception) as exc:
        calculator.calculate(mock_request)
    assert str(exc.value) == "Invalid request"
    

