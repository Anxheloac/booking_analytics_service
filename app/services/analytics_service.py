from typing import Any, Dict, List
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.booking import Booking
from app.enums.booking_status import BookingStatus


class AnalyticsService:
    """
    Service class responsible for performing analytics operations on bookings data.

    This service provides methods to query booking statistics such as total bookings,
    get_cancellation_rate, and revenue grouped by property. It interacts with the
    database session to execute these queries asynchronously.

    Attributes:
        db (AsyncSession): The asynchronous database session used to perform queries.
    """

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_revenue_by_property(self) -> List[Dict[str, Any]]:
        stmt = (
            select(
                Booking.property_code,
                func.sum(Booking.total_amount).label("total_revenue")
            )
            .where(Booking.status == BookingStatus.CONFIRMED.value)
            .group_by(Booking.property_code)
        )
        result = await self.db.execute(stmt)
        rows = result.all()
        return [{"property_id": row.property_code, "revenue": row.total_revenue} for row in rows]

    async def get_cancellation_rate(self) -> Dict[str, float]:
        total_stmt = select(func.count()).select_from(Booking)
        canceled_stmt = select(func.count()).select_from(Booking).where(Booking.status == BookingStatus.CANCELLED.value)

        total_result = await self.db.execute(total_stmt)
        canceled_result = await self.db.execute(canceled_stmt)

        total = total_result.scalar_one()
        canceled = canceled_result.scalar_one()

        if total == 0:
            return {"cancellation_rate": 0.0}
        return {"cancellation_rate": round((canceled / total) * 100, 2)}

    async def get_bookings_by_source(self) -> List[Dict]:
        stmt = select(Booking.source, func.count()).group_by(Booking.source)
        result = await self.db.execute(stmt)
        rows = result.all()
        return [{"source": row[0], "count": row[1]} for row in rows]
