from typing import Dict, List
from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler:
    def standard_deviation(self, numbers: List[float]) -> float:
        return 1
    
def test_calculate_integration():
    mock_request = MockRequest({ "numbers": [1, 1, 1, 1, 2]})
    
    calculator_2 = Calculator2(NumpyHandler())
    result = calculator_2.calculate(mock_request)
    assert "data" in result
    assert "calculator" in result["data"]
    assert "result" in result["data"]
    assert result["data"]["calculator"] == 2
    assert result["data"]["result"] == 2.68
    
def test_calculate():
    mock_request = MockRequest({ "numbers": [1, 1, 1, 1, 2]})
    
    calculator_2 = Calculator2(MockDriverHandler())
    result = calculator_2.calculate(mock_request)
    assert "data" in result
    assert "calculator" in result["data"]
    assert "result" in result["data"]
    assert result["data"]["calculator"] == 2
    assert result["data"]["result"] == 1.0
    