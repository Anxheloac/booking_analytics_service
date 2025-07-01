from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import time

from app.core.exceptions.api_exceptions import TooManyRequestsException


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests: int = 10, window_seconds: int = 60):
        super().__init__(app)
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.ip_timestamps = {}

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        now = time.time()
        timestamps = self.ip_timestamps.get(client_ip, [])

        # Remove outdated timestamps
        timestamps = [ts for ts in timestamps if now - ts < self.window_seconds]
        timestamps.append(now)
        self.ip_timestamps[client_ip] = timestamps

        if len(timestamps) > self.max_requests:
            raise TooManyRequestsException()

        response = await call_next(request)
        return response
