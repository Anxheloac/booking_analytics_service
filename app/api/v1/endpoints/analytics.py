from typing import List
from fastapi import APIRouter, Depends

from app.dependencies import get_analytics_service
from app.api.v1.schemas.analytics import RevenueByPropertyResponse, CancellationRateResponse, BookingsBySourceResponse
from app.services.analytics_service import AnalyticsService


router = APIRouter()


@router.get("/revenue-by-property", response_model=List[RevenueByPropertyResponse])
async def revenue_by_property(analytics_service: AnalyticsService = Depends(get_analytics_service)):
    return await analytics_service.get_revenue_by_property()


@router.get("/cancellation-rate", response_model=CancellationRateResponse)
async def cancellation_rate(analytics_service: AnalyticsService = Depends(get_analytics_service)):
    return await analytics_service.get_cancellation_rate()


@router.get("/bookings-by-source", response_model=List[BookingsBySourceResponse])
async def bookings_by_source(analytics_service: AnalyticsService = Depends(get_analytics_service)):
    return await analytics_service.get_bookings_by_source()
