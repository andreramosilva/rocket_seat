from calculator_1 import Calculator1
from typing import Dict
from pytest import raises

class MockRequest:
    def __init__(self,body:Dict)->None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={"number": 1})
    calculator = Calculator1()
    
    response = calculator.calculate(mock_request)
    print(response)

    # formato da resposta
    assert "data" in response
    assert "calculator" in response["data"]
    assert "result" in response["data"]

    # assertividade da resposta
    assert response["data"]["calculator"] == 1
    assert response["data"]["result"] == 14.25

def teste_calculate_invalid_body():
    mock_request = MockRequest(body={})
    calculator = Calculator1()
    
    with raises(Exception) as exceptioninfo:
        calculator.calculate(mock_request)

    assert str(exceptioninfo.value) == "Body mal formatado"