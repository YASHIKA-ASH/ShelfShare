from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.services.rental_service import (
    borrow_book,
    return_book,
    my_books,
    rate_book
)

from app.schemas.rental import (
    RentalCreate,
    RatingRequest
)

router = APIRouter(
    prefix="/rentals",
    tags=["Rentals"]
)


@router.post("/borrow")
def borrow(
    rental: RentalCreate,
    db: Session = Depends(get_db)
):
    return borrow_book(db, rental)


@router.post("/return/{rental_id}")
def return_rental(
    rental_id: int,
    db: Session = Depends(get_db)
):
    return return_book(db, rental_id)


@router.get("/my-books/{user_id}")
def get_my_books(
    user_id: int,
    db: Session = Depends(get_db)
):
    return my_books(db, user_id)


@router.post("/rate")
def rate(
    request: RatingRequest,
    db: Session = Depends(get_db)
):
    return rate_book(
        db,
        request.rental_id,
        request.rating
    )