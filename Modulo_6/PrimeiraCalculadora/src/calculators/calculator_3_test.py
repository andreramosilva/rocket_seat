from src.drivers.numpy_handler import NumpyHandler
from .calculator_3 import Calculator3
from typing import Dict , List
from pytest import raises

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler():
    def variance(self, data: List[float])->float:
        return 1596.16

def test_calculate_with_variance_error():
    mock_request = MockRequest({"numbers":[1,2,3,4,5]})
    calculator = Calculator3(NumpyHandler())

    with raises (Exception) as exc:
        calculator.calculate(mock_request)

    assert str(exc.value) == "Variance is lower than multiplication"

def test_calculate():
    mock_request = MockRequest({"numbers":[1,1,1,1,100]})
    calculator = Calculator3(MockDriverHandler())
    calc = calculator.calculate(mock_request)
    print(calc)
    assert calc == {"data": {"calculator": 3, "result": 1596.16, "success": True}}
