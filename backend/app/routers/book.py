from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.book_service import available_books
from app.schemas.book_confirm import BookConfirmRequest

from app.dependencies import get_db
from app.schemas.book import BookCreate, BookResponse
from app.services.book_service import create_book
from app.services.book_confirm_service import confirm_book as confirm_book_service
router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


@router.post("/", response_model=BookResponse)
def upload_book(
    book: BookCreate,
    db: Session = Depends(get_db)
):
    return create_book(
        db,
        book,
        owner_id=1
    )

@router.post("/confirm")
def confirm_book(
    book: BookConfirmRequest,
    db: Session = Depends(get_db)
):

    saved_book = confirm_book_service(
        db=db,
        data=book,
        owner_id=1
    )

    return saved_book

@router.get("/available")
def get_available_books(
    db: Session = Depends(get_db)
):

    return available_books(db)