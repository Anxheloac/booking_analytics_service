import pytest
from unittest.mock import AsyncMock, MagicMock
from app.services.analytics_service import AnalyticsService

@pytest.mark.asyncio
async def test_get_revenue_by_property():
    # Arrange
    mock_db = MagicMock()
    # Prepare mock rows returned by execute().all()
    mock_db.execute = AsyncMock(return_value=MagicMock(all=MagicMock(return_value=[
        MagicMock(property_code="P001", total_revenue=1000.0),
        MagicMock(property_code="P002", total_revenue=2500.0),
    ])))

    service = AnalyticsService(db=mock_db)

    # Act
    result = await service.get_revenue_by_property()

    # Assert
    assert isinstance(result, list)
    assert result == [
        {"property_id": "P001", "revenue": 1000.0},
        {"property_id": "P002", "revenue": 2500.0},
    ]
    mock_db.execute.assert_called_once()  # You can also check the actual SQL if you want

@pytest.mark.asyncio
async def test_get_cancellation_rate_zero_total():
    mock_db = MagicMock()
    # Mock total bookings count = 0
    mock_db.execute = AsyncMock(side_effect=[
        MagicMock(scalar_one=MagicMock(return_value=0)),  # total_stmt
        MagicMock(scalar_one=MagicMock(return_value=0)),  # canceled_stmt
    ])

    service = AnalyticsService(db=mock_db)

    result = await service.get_cancellation_rate()

    assert result == {"cancellation_rate": 0.0}
    assert mock_db.execute.call_count == 2

@pytest.mark.asyncio
async def test_get_cancellation_rate_nonzero():
    mock_db = MagicMock()
    # Mock total bookings count = 100, canceled = 25
    mock_db.execute = AsyncMock(side_effect=[
        MagicMock(scalar_one=MagicMock(return_value=100)),  # total_stmt
        MagicMock(scalar_one=MagicMock(return_value=25)),   # canceled_stmt
    ])

    service = AnalyticsService(db=mock_db)

    result = await service.get_cancellation_rate()

    assert result == {"cancellation_rate": 25.0}
    assert mock_db.execute.call_count == 2

@pytest.mark.asyncio
async def test_get_bookings_by_source():
    mock_db = MagicMock()
    mock_db.execute = AsyncMock(return_value=MagicMock(all=MagicMock(return_value=[
        ("online", 10),
        ("phone", 5),
    ])))

    service = AnalyticsService(db=mock_db)

    result = await service.get_bookings_by_source()

    assert isinstance(result, list)
    assert result == [
        {"source": "online", "count": 10},
        {"source": "phone", "count": 5},
    ]
    mock_db.execute.assert_called_once()
