from datetime import datetime
from sqlalchemy import DateTime, Float, String
from sqlalchemy.orm import Mapped, mapped_column, declarative_base

from app.enums.booking_source import BookingSource
from app.enums.booking_status import BookingStatus

Base = declarative_base()


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    property_code: Mapped[str] = mapped_column(String, index=True)
    guest_email: Mapped[str] = mapped_column(String, index=True)
    check_in: Mapped[datetime] = mapped_column(DateTime)
    check_out: Mapped[datetime] = mapped_column(DateTime)
    total_amount: Mapped[float] = mapped_column(Float)
    source: Mapped[str] = mapped_column(String, default=BookingStatus.CONFIRMED.value)
    status: Mapped[str] = mapped_column(String, default=BookingSource.PMS.value)
