from src.calculators.calculator_2 import Calculator2
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_hander_interface import DriverHandlerInterface


class MockRequest:
    def __init__(self, body: Dict)->None    :
        self.json = body
    
class MockDriverHandler(DriverHandlerInterface):
    def standard_deviation(self, data: List[float])->float:
        return 0.14

# integraçao entre numpyhandler e calculator2
def test_calculate_integration():
    mock_request = MockRequest({"numbers": [1, 2, 3]})

    driver = NumpyHandler()
    calculator = Calculator2(driver)
    result = calculator.calculate(mock_request)

    assert isinstance(result, dict)
    assert result == { "data": { "calculator": 2, "result": 0.14 }}
    
    
def test_calculate():
    mock_request = MockRequest({"numbers": [1, 2, 3]})

    driver = MockDriverHandler()
    calculator = Calculator2(driver)
    result = calculator.calculate(mock_request)

    assert isinstance(result, dict)
    assert result == { "data": { "calculator": 2, "result": 7.14 }}