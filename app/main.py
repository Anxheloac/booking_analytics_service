from fastapi import FastAPI

from app.api.v1.endpoints import bookings, analytics
from app.core.exceptions.handlers import generic_exception_handler
from app.core.middleware.api_rate_limit import RateLimitMiddleware
from app.core.middleware.ip_whitelist import IPWhitelistMiddleware

app = FastAPI(
    title="Booking and Analytics API",
    description="API to analyze property bookings and show analytics",
    version="1.0.0",
    terms_of_service="https://example.com/terms/",
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    }
)

# Configure middlewares
app.add_middleware(RateLimitMiddleware, max_requests=100, window_seconds=60)
app.add_middleware(IPWhitelistMiddleware, whitelist={"127.0.0.1", "your.other.ip"})

# Include the router with a prefix and tags for OpenAPI docs
app.include_router(bookings.router, prefix="/api/v1/bookings", tags=["bookings"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["analytics"])

# Register global exception handlers
app.add_exception_handler(Exception, generic_exception_handler)
