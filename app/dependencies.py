from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_async_db
from app.services.analytics_service import AnalyticsService
from app.services.booking_service import BookingService


async def get_analytics_service(db: AsyncSession = Depends(get_async_db)) -> AnalyticsService:
    return AnalyticsService(db)


async def get_booking_service(db: AsyncSession = Depends(get_async_db)) -> BookingService:
    return BookingService(db)
