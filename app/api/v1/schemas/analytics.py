from pydantic import BaseModel


class RevenueByPropertyResponse(BaseModel):
    property_id: str
    revenue: float


class CancellationRateResponse(BaseModel):
    cancellation_rate: float  # percentage (e.g., 13.33)


class BookingsBySourceResponse(BaseModel):
    source: str
    count: int
