from sqlalchemy.orm import Session
from app.models.book import Book
from app.models.book_copy import BookCopy
from app.schemas.book import BookCreate


def create_book(
    db: Session,
    book: BookCreate,
    owner_id: int
):

    new_book = Book(
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

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


def available_books(db: Session):

    books = (
        db.query(Book)
        .join(BookCopy)
        .filter(BookCopy.status == "Available")
        .all()
    )

    return books