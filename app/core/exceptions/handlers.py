from fastapi import Request
from fastapi.responses import JSONResponse


async def generic_exception_handler(request: Request, exc: Exception):
    # Log the actual error (optional)

    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": "An internal error occurred. Please try again later.",
            "detail": str(exc)  # Optional: remove in production for security
        },
    )
