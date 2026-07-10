from sqlalchemy.orm import Session

from app.models.book import Book
from app.models.book_copy import BookCopy


def create_book_copies(
    db: Session,
    book_id: int,
    data
):

    book = db.query(Book).filter(
        Book.id == book_id
    ).first()

    if not book:
        return {
            "message": "Book not found"
        }

    copies = []

    last_copy = db.query(BookCopy).count()

    for i in range(data.number_of_copies):

        barcode = f"BK{last_copy + i + 1:06}"

        copy = BookCopy(
            book_id=book_id,
            barcode=barcode,
            rack=data.rack,
            status="Available",
            condition="Good"
        )

        db.add(copy)

        copies.append(copy)

    db.commit()

    return copies

def get_book_copies(
    db: Session,
    book_id: int
):

    copies = db.query(BookCopy).filter(
        BookCopy.book_id == book_id
    ).all()

    return copies