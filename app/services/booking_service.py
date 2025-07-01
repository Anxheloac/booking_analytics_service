from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.booking import Booking
from app.core.exceptions.booking_exceptions import BookingException


class BookingService:
    """
    Service class responsible for booking-related operations.

    This service handles creating new bookings in the database,
    ensuring proper transaction management with commit and rollback.

    Args:
        db (AsyncSession): The asynchronous SQLAlchemy session for database operations.
    """

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_booking(self, data) -> Booking:
        booking = Booking(**data.model_dump())
        self.db.add(booking)

        try:
            await self.db.commit()
            await self.db.refresh(booking)
        except Exception as e:
            await self.db.rollback()
            raise BookingException(f"Failed to create booking: {str(e)}", status.HTTP_500_INTERNAL_SERVER_ERROR)

        return booking
