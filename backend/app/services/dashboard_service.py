from sqlalchemy.orm import Session

from app.models.user import User
from app.models.book import Book
from app.models.book_copy import BookCopy
from app.models.rental import Rental
from app.models.wishlist import Wishlist
from app.models.reservation import Reservation

def dashboard_stats(db: Session):

    total_users = db.query(User).count()

    total_books = db.query(Book).count()
    total_reservations = db.query(Reservation).count()
    total_copies = db.query(BookCopy).count()
    reservation_count = db.query(Reservation).count()
    available_copies = db.query(BookCopy).filter(
        BookCopy.status == "Available"
    ).count()

    borrowed_books = db.query(BookCopy).filter(
        BookCopy.status == "Borrowed"
    ).count()

    active_rentals = db.query(Rental).count()

    returned_books = db.query(BookCopy).filter(
        BookCopy.status == "Returned"
    ).count()

    wishlist_items = db.query(Wishlist).count()

    return {

        "total_users": total_users,

        "total_books": total_books,

        "total_copies": total_copies,

        "available_copies": available_copies,

        "borrowed_books": borrowed_books,

        "total_reservations": total_reservations,

        "active_rentals": active_rentals,

        "returned_books": returned_books,

        "wishlist_items": wishlist_items

    }