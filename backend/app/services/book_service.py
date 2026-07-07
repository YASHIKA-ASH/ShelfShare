from sqlalchemy.orm import Session

from app.models.book import Book
from app.schemas.book import BookCreate
from app.models.rental import Rental

def create_book(
    db: Session,
    book: BookCreate,
    owner_id: int
):

    db_book = Book(
        title=book.title,
        author=book.author,
        isbn=book.isbn,
        publisher=book.publisher,
        edition=book.edition,
        subject=book.subject,
        branch=book.branch,
        semester=book.semester,
        description=book.description,
        image_url=book.image_url,
        owner_id=owner_id
    )

    db.add(db_book)

    db.commit()

    db.refresh(db_book)

    return db_book

def available_books(db: Session):

    rented_ids = db.query(
        Rental.book_id
    ).filter(
        Rental.status == "Borrowed"
    )

    books = db.query(Book).filter(
        ~Book.id.in_(rented_ids)
    ).all()

    return books