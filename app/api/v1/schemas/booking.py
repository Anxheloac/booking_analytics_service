from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator

from app.enums.booking_source import BookingSource
from app.enums.booking_status import BookingStatus


class BookingCreate(BaseModel):
    property_code: str = Field(..., min_length=1, description="Property external unique code")
    guest_email: EmailStr = Field(..., description="Guest's email address")
    check_in: datetime = Field(..., description="Booking check-in date and time")
    check_out: datetime = Field(..., description="Booking check-out date and time")
    total_amount: float = Field(..., description="Total amount for the booking")
    source: Optional[BookingSource] = BookingSource.DIRECT
    status: Optional[BookingStatus] = BookingStatus.CONFIRMED

    @field_validator('check_out')
    def check_check_out_after_check_in(cls, v, info):
        check_in = info.data.get('check_in')
        if check_in and v <= check_in:
            raise ValueError("check_out must be after check_in")
        return v


class BookingResponse(BaseModel):
    id: int
    property_code: str
    guest_email: EmailStr
    check_in: datetime
    check_out: datetime
    total_amount: float
    status: BookingStatus
    source: BookingSource
