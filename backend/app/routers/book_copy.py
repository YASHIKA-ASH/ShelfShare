from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.dependencies import get_db

from app.schemas.book_copy import (
    BookCopyCreate,
    BookCopyResponse
)

from app.services.book_copy import (
    create_book_copies
)

router = APIRouter(
    prefix="/books",
    tags=["Book Copies"]
)


@router.post(
    "/{book_id}/copies",
    response_model=List[BookCopyResponse]
)
def add_copies(
    book_id: int,
    request: BookCopyCreate,
    db: Session = Depends(get_db)
):

    return create_book_copies(
        db,
        book_id,
        request
    )