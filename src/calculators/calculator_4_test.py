from typing import Dict, List
from pytest import raises
from .calculator_4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler: 
    def mean(self, numbers: List[float]) -> float:
        return 1
    
    
def test_calculate():
    mock_request = MockRequest({ "numbers": [1, 1, 1, 1, 0.1]})
    
    calculator_4 = Calculator4(MockDriverHandler())
    result = calculator_4.calculate(mock_request)
    assert "data" in result
    assert "calculator" in result["data"]
    assert "result" in result["data"]
    assert result["data"]["calculator"] == 4
    assert result["data"]["result"] == 1


def test_calculate_with_error():
    mock_request = MockRequest({ "numbersss": [1, 1, 1, 1, 2]})

    calculator_4 = Calculator4(MockDriverHandler())

    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)

    assert str(excinfo.value) == 'body mal formatado'
    

def test_calculate_integration():
    mock_request = MockRequest({ "numbers": [1, 2, 3, 4, 5]})
    
    calculator_4 = Calculator4(NumpyHandler())
    result = calculator_4.calculate(mock_request)

    assert "data" in result
    assert "calculator" in result["data"]
    assert "result" in result["data"]
    assert "success" in result["data"]
    assert result["data"]["calculator"] == 4
    assert result["data"]["result"] == 3
    assert result["data"]["success"]
