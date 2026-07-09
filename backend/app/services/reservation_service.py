from sqlalchemy.orm import Session

from app.models.user import User
from app.models.book import Book
from app.models.book_copy import BookCopy
from app.models.rental import Rental
from app.models.wishlist import Wishlist
from app.models.reservation import Reservation


def dashboard_stats(db: Session):

    # -------------------------
    # Cards
    # -------------------------

    total_users = db.query(User).count()

    total_books = db.query(Book).count()

    available_copies = db.query(BookCopy).filter(
        BookCopy.status == "Available"
    ).count()

    borrowed_books = db.query(BookCopy).filter(
        BookCopy.status == "Borrowed"
    ).count()

    total_reservations = db.query(Reservation).count()

    pending_reservations = db.query(Reservation).filter(
        Reservation.status == "Waiting"
    ).count()

    total_wishlist = db.query(Wishlist).count()

    # -------------------------
    # Popular Book
    # -------------------------

    popular_book = "N/A"

    rental_counts = {}

    rentals = db.query(Rental).all()

    for rental in rentals:

        copy = db.query(BookCopy).filter(
            BookCopy.id == rental.copy_id
        ).first()

        if copy:

            rental_counts[copy.book_id] = rental_counts.get(copy.book_id, 0) + 1

    if rental_counts:

        most_borrowed = max(
            rental_counts,
            key=rental_counts.get
        )

        book = db.query(Book).filter(
            Book.id == most_borrowed
        ).first()

        if book:

            popular_book = book.title

    # -------------------------
    # Active User
    # -------------------------

    active_user = "N/A"

    if total_users > 0:

        active_user = db.query(User).first().full_name

    # -------------------------
    # Recent Books
    # -------------------------

    recent_books = []

    books = db.query(Book).order_by(
        Book.created_at.desc()
    ).limit(5).all()

    for book in books:

        available = db.query(BookCopy).filter(
            BookCopy.book_id == book.id,
            BookCopy.status == "Available"
        ).count()

        recent_books.append({

            "title": book.title,

            "author": book.author,

            "subject": book.subject,

            "availability": f"{available} Available"

        })

    # -------------------------
    # Recent Activity
    # -------------------------

    recent_activity = []

    rentals = db.query(Rental).order_by(
        Rental.id.desc()
    ).limit(5).all()

    for rental in rentals:

        user = db.query(User).filter(
            User.id == rental.user_id
        ).first()

        copy = db.query(BookCopy).filter(
            BookCopy.id == rental.copy_id
        ).first()

        title = "Unknown"

        if copy:

            book = db.query(Book).filter(
                Book.id == copy.book_id
            ).first()

            if book:
                title = book.title

        recent_activity.append({

            "time": "Recently",

            "user": user.full_name if user else "Unknown",

            "action": f"Borrowed '{title}'"

        })

    # -------------------------
    # Response
    # -------------------------

    return {

        "total_books": total_books,

        "available_copies": available_copies,

        "borrowed_books": borrowed_books,

        "total_reservations": total_reservations,

        "pending_reservations": pending_reservations,

        "total_wishlist": total_wishlist,

        "popular_book": popular_book,

        "active_user": active_user,

        "recent_books": recent_books,

        "recent_activity": recent_activity

    }