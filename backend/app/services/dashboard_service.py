from sqlalchemy.orm import Session

from app.models.user import User
from app.models.book import Book
from app.models.rental import Rental
from app.models.wishlist import Wishlist


def dashboard_stats(db: Session):

    total_users = db.query(User).count()

    total_books = db.query(Book).count()

    available_books = 0
    borrowed_books = 0

    wishlist_items = db.query(Wishlist).count()

    return {
        "total_users": total_users,
        "total_books": total_books,
        "available_books": available_books,
        "borrowed_books": borrowed_books,
        "active_rentals": active_rentals,
        "returned_books": returned_books,
        "wishlist_items": wishlist_items
    }