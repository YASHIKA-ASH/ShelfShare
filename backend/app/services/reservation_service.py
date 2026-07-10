from sqlalchemy.orm import Session
from app.models.book import Book
from app.models.reservation import Reservation
from app.models.book import Book
from app.schemas.reservation import ReservationCreate


def reserve_book(db: Session, reservation: ReservationCreate):

    # Check if book exists
    book = db.query(Book).filter(
        Book.id == reservation.book_id
    ).first()

    if not book:
        return {
            "message": "Book not found"
        }

    # Find next queue position
    last_reservation = (
        db.query(Reservation)
        .filter(Reservation.book_id == reservation.book_id)
        .order_by(Reservation.queue_position.desc())
        .first()
    )

    queue_position = 1

    if last_reservation:
        queue_position = last_reservation.queue_position + 1

    new_reservation = Reservation(
        user_id=reservation.user_id,
        book_id=reservation.book_id,
        queue_position=queue_position,
        status="Waiting"
    )

    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)

    return {
        "message": "Book reserved successfully",
        "reservation_id": new_reservation.id,
        "queue_position": queue_position,
        "status": new_reservation.status
    }
def get_user_reservations(db: Session, user_id: int):

    reservations = (
        db.query(Reservation)
        .filter(Reservation.user_id == user_id)
        .all()
    )

    result = []

    for reservation in reservations:

        book = db.query(Book).filter(
            Book.id == reservation.book_id
        ).first()

        result.append({

            "id": reservation.id,

            "title": book.title if book else "Unknown",

            "author": book.author if book else "Unknown",

            "position": reservation.queue_position,

            "status": reservation.status

        })

    return result