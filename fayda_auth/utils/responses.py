class SuccessResponse:
    def __init__(self, message: str, data: any, status_code: int):
        self.message = message
        self.data = data
        self.status_code = status_code

    def __dict__(self):
        return {"message": self.message, "data": self.data, "status_code": self.status_code}

class ErrorResponse:
    def __init__(self, error_message: str, status_code: int):
        self.error_message = error_message
        self.status_code = status_code

    def __dict__(self):
        return {"error_message": self.error_message, "status_code": self.status_code}