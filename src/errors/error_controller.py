from typing import Dict
from .http_unprocessable_entity import HttpUnprocessableEntityError
from .http_bad_request import HttpBadRequestError

def handle_errors(error: Exception) -> Dict:
    if isinstance(error, (HttpBadRequestError, HttpUnprocessableEntityError)):
        return {
            "status_code": error.status_code,
            "body": {
                "errors": [{
                    "title": error.name,
                    "message": error.message
                }]
            }
            
        }
    
    return {
        "status_code": 500,
        "body": {
            "errors": [{
                "title": "Internal Server Error",
                "message": str(error)
            }]
        }
    }