from flask import request as FlaskRequest
from typing import Dict, List
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequestError
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler
        
    def calculate(self, request: FlaskRequest) -> Dict:  #type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        variance = self.__driver_handler.variance(input_data)
        multiplication = self.__calcualte_multiplication(input_data)
        self.__verify_results(variance, multiplication)

        return self.__format_response(variance)

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body or len(body["numbers"]) < 2:
            raise HttpUnprocessableEntityError("body mal formatado")
        
        input_data = body["numbers"]
        return input_data
    
    def __calcualte_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1

        for num in numbers: multiplication *= num

        return multiplication
    
    def __verify_results(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise HttpBadRequestError('Falha no processo: Variância menor que a mulitiplicação')
    
    def __format_response(self, variance: float) -> Dict:
        return {
            "data": {
                "calculator": 3,
                "result": round(variance, 5),
                "success": True
            }
        }
