import pytest
from unittest.mock import AsyncMock, MagicMock
from fastapi import status

from app.core.exceptions.booking_exceptions import BookingException
from app.enums.booking_source import BookingSource
from app.services.booking_service import BookingService
from app.api.v1.schemas.booking import BookingCreate

@pytest.mark.asyncio
async def test_create_booking_success():
    mock_db = MagicMock()
    mock_db.add = MagicMock()
    mock_db.commit = AsyncMock()
    mock_db.refresh = AsyncMock()

    service = BookingService(db=mock_db)
    booking_data = BookingCreate(
        property_code="XYN",
        guest_email="test@example.com",
        check_in="2025-08-01T14:00:00",
        check_out="2025-08-05T11:00:00",
        source=BookingSource.PMS.value
    )

    result = await service.create_booking(booking_data)
    assert result is not None
    mock_db.commit.assert_awaited()

@pytest.mark.asyncio
async def test_create_booking_raises_booking_exception_on_commit_failure():
    # Arrange: create a mock AsyncSession
    mock_db = MagicMock()
    mock_db.add = MagicMock()
    mock_db.commit = AsyncMock(side_effect=Exception("DB commit failed"))
    mock_db.refresh = AsyncMock()
    mock_db.rollback = AsyncMock()

    service = BookingService(db=mock_db)
    booking_data = BookingCreate(
        property_code="XYN",
        guest_email="test@example.com",
        check_in="2025-08-01T14:00:00",
        check_out="2025-08-05T11:00:00",
        source=BookingSource.PMS.value
    )

    # Act & Assert
    with pytest.raises(BookingException) as booking_exception:
        await service.create_booking(booking_data)

    exception = booking_exception.value

    assert "Failed to create booking" in str(exception)
    assert exception.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    # Check rollback was called
    mock_db.rollback.assert_awaited_once()
