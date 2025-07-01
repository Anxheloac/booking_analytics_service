from fastapi import APIRouter, Depends, status

from app.api.v1.schemas.booking import BookingCreate, BookingResponse
from app.dependencies import get_booking_service
from app.services.booking_service import BookingService


router = APIRouter()


@router.post("", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
async def create(
    data: BookingCreate,
    booking_service: BookingService = Depends(get_booking_service)
):
    return await booking_service.create_booking(data)
