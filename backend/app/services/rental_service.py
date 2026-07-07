from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import date

from app.models.book import Book
from app.models.book_copy import BookCopy
from app.models.rental import Rental


def borrow_book(db: Session, data):

    # Check if book exists
    book = db.query(Book).filter(
        Book.id == data.book_id
    ).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    # Find first available copy
    copy = db.query(BookCopy).filter(
        BookCopy.book_id == data.book_id,
        BookCopy.status == "Available"
    ).first()

    if not copy:
        raise HTTPException(
            status_code=400,
            detail="No copies available"
        )

    # Create rental
    rental = Rental(
        user_id=data.user_id,
        copy_id=copy.id,
        issue_date=data.issue_date,
        due_date=data.due_date,
        status="Borrowed"
    )

    # Update copy status
    copy.status = "Borrowed"

    db.add(rental)
    db.commit()
    db.refresh(rental)

    return rental


def return_book(db: Session, rental_id: int):

    rental = db.query(Rental).filter(
        Rental.id == rental_id
    ).first()

    if not rental:
        raise HTTPException(
            status_code=404,
            detail="Rental not found"
        )

    rental.return_date = date.today()
    rental.status = "Returned"

    copy = db.query(BookCopy).filter(
        BookCopy.id == rental.copy_id
    ).first()

    if copy:
        copy.status = "Available"

    db.commit()
    db.refresh(rental)

    return rental


def my_books(db: Session, user_id: int):

    rentals = db.query(Rental).filter(
        Rental.user_id == user_id
    ).all()

    return rentals


def rate_book(db: Session, rental_id: int, rating: int):

    rental = db.query(Rental).filter(
        Rental.id == rental_id
    ).first()

    if not rental:
        raise HTTPException(
            status_code=404,
            detail="Rental not found"
        )

    rental.rating = rating

    db.commit()
    db.refresh(rental)

    return rental