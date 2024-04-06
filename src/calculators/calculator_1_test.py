from typing import Dict, List
from pytest import raises
from .calculator_1 import Calculator1

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={ "number": 1})
    calculator_1 = Calculator1()

    response = calculator_1.calculate(mock_request)
    assert "data" in response
    assert "calculator" in response["data"]
    assert "result" in response["data"]

    assert response["data"]["result"] == 14.25
    assert response["data"]["calculator"] == 1

def test_calculate_invalid_body():
    mock_request = MockRequest(body={ "invalid_data": 1 })
    calculator_1 = Calculator1()

    with raises(Exception) as e_info:
        calculator_1.calculate(mock_request)
    
    assert str(e_info.value) == "body mal formatado"


