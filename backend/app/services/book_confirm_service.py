from sqlalchemy.orm import Session

from app.models.book import Book


def confirm_book(
    db: Session,
    data,
    owner_id: int
):

    book = Book(
        title=data.title,
        author=data.author,
        isbn=data.isbn,
        publisher=data.publisher,
        edition=data.edition,
        subject=data.subject,
        branch=data.branch,
        semester=data.semester,
        description=data.description,
        image_url=data.image_url,
        owner_id=owner_id
    )

    db.add(book)

    db.commit()

    db.refresh(book)

    return book