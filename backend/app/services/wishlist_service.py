from sqlalchemy.orm import Session

from app.models.book import Book
from app.models.wishlist import Wishlist


def add_to_wishlist(
    db: Session,
    user_id: int,
    data
):
   
    exists = db.query(Wishlist).filter(
        Wishlist.user_id == user_id,
        Wishlist.book_id == data.book_id
    ).first()

    if exists:
     raise HTTPException(
        status_code=409,
        detail="Book already in wishlist"
    )

   
    item = Wishlist(
        user_id=user_id,
        book_id=data.book_id
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


def get_wishlist(
    db: Session,
    user_id: int
):
    wishlist = db.query(Wishlist).filter(
        Wishlist.user_id == user_id
    ).all()

    return wishlist


def remove_wishlist(
    db: Session,
    wishlist_id: int
):
    item = db.query(Wishlist).filter(
        Wishlist.id == wishlist_id
    ).first()

    if not item:
     raise HTTPException(
        status_code=404,
        detail="Wishlist item not found"
    )
def recommend_books(
    db: Session,
    user_id: int
):
    wishlist = db.query(Wishlist).filter(
        Wishlist.user_id == user_id
    ).all()

    if not wishlist:
        return []

    subjects = []
    wishlist_book_ids = []

    for item in wishlist:
        if item.book:
            subjects.append(item.book.subject)
            if book:
                subjects.append(book.subject)
                wishlist_book_ids.append(book.id)

    recommendations = db.query(Book).filter(
        Book.subject.in_(subjects),
        ~Book.id.in_(wishlist_book_ids)
    ).all()

    return recommendations