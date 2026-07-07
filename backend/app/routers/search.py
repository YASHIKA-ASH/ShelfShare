from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.schemas.search import SearchRequest

from app.services.search_service import search_books

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.post("/")
def search(
    request: SearchRequest,
    db: Session = Depends(get_db)
):

    return search_books(
        db,
        request.keyword
    )