from typing import Dict
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator1:
    def calculate(self, request: FlaskRequest) -> Dict:  #type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        division_result = input_data / 3

        first_process = self.__first_process(division_result)
        second_process = self.__second_process(division_result)
        third_process = self.__third_process(division_result)

        result = first_process + second_process + third_process

        return self.__format_response(result)

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise HttpUnprocessableEntityError("body mal formatado")
        
        input_data = body["number"]
        return input_data
    
    def __first_process(self, number: float) -> float:
        first_part = (number / 4) + 7
        second_part = (first_part ** 2) * 0.257
        return second_part
    
    def __second_process(self, number: float) -> float:
        first_part = number ** 2.121
        second_part = (first_part / 5) + 1
        return second_part
    
    def __third_process(self, number: float) -> float:
        return number
    
    def __format_response(self, result: float) -> Dict:
        return {
            "data": {
                "calculator": 1,
                "result": round(result, 2)
            }
        }
