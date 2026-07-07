from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.schemas.reservation import ReservationCreate
from app.services.reservation_service import reserve_book

router = APIRouter(
    prefix="/reservations",
    tags=["Reservations"]
)


@router.post("/")
def create_reservation(
    reservation: ReservationCreate,
    db: Session = Depends(get_db)
):
    return reserve_book(db, reservation)