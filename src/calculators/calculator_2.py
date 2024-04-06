from flask import request as FlaskRequest
from typing import Dict, List
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler
        
    def calculate(self, request: FlaskRequest) -> Dict:  #type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        result = self.__process_data(input_data)

        return self.__format_response(result)

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body or len(body["numbers"]) < 2:
            raise HttpUnprocessableEntityError("body mal formatado")
        
        input_data = body["numbers"]
        return input_data
    
    def __process_data(self, numbers: List[float]) -> float:
        first_process = [(num * 1) ** 0.95 for num in numbers]
        result = self.__driver_handler.standard_deviation(first_process)

        return 1/result
    
    def __format_response(self, result: float) -> Dict:
        return {
            "data": {
                "calculator": 2,
                "result": round(result, 2)
            }
        }    
