from fastapi import HTTPException, status


class ForbiddenIPException(HTTPException):
    def __init__(self, detail: str = "Forbidden IP"):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)


class TooManyRequestsException(HTTPException):
    def __init__(self, detail: str = "Too many requests"):
        super().__init__(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=detail)
