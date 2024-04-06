from typing import Dict, List
from pytest import raises
from .calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler: 
    def variance(self, numbers: List[float]) -> float:
        return 1
    
    
def test_calculate():
    mock_request = MockRequest({ "numbers": [1, 1, 1, 1, 0.1]})
    
    calculator_3 = Calculator3(MockDriverHandler())
    result = calculator_3.calculate(mock_request)
    assert "data" in result
    assert "calculator" in result["data"]
    assert "result" in result["data"]
    assert result["data"]["calculator"] == 3
    assert result["data"]["result"] == 1


def test_calculate_with_error():
    mock_request = MockRequest({ "numbers": [1, 1, 1, 1, 2]})

    calculator_3 = Calculator3(MockDriverHandler())

    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

    assert str(excinfo.value) == 'Falha no processo: Variância menor que a mulitiplicação'
    

def test_calculate_integration():
    mock_request = MockRequest({ "numbers": [0.1, -2, 3, 4, 5]})
    
    calculator_3 = Calculator3(NumpyHandler())
    result = calculator_3.calculate(mock_request)

    assert "data" in result
    assert "calculator" in result["data"]
    assert "result" in result["data"]
    assert "success" in result["data"]
    assert result["data"]["calculator"] == 3
    assert result["data"]["result"] == 6.7216
    assert result["data"]["success"]
   
    
def test_calculate_integration_variance_error():
    mock_request = MockRequest({ "numbers": [1, 2, 3, 4, 5]})
    
    calculator_3 = Calculator3(NumpyHandler())

    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

    assert str(excinfo.value) == 'Falha no processo: Variância menor que a mulitiplicação'
