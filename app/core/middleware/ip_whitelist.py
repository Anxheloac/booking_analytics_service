from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.exceptions.api_exceptions import ForbiddenIPException


class IPWhitelistMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, whitelist: set[str]):
        super().__init__(app)
        self.whitelist = whitelist

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        if client_ip not in self.whitelist:
            raise ForbiddenIPException()
        
        return await call_next(request)
