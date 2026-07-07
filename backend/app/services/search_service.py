from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models.book import Book


def search_books(db: Session, keyword: str):

    books = db.query(Book).filter(

        or_(

            Book.title.ilike(f"%{keyword}%"),

            Book.author.ilike(f"%{keyword}%"),

            Book.subject.ilike(f"%{keyword}%"),

            Book.publisher.ilike(f"%{keyword}%"),

            Book.branch.ilike(f"%{keyword}%")

        )

    ).all()

    return books