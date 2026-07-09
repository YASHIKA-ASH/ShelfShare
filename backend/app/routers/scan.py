from fastapi import APIRouter, UploadFile, File

from app.services.scan_service import scan_book
from app.schemas.book_scan import BookScanResponse

router = APIRouter(
    prefix="/scan",
    tags=["AI Scan"]
)


@router.post("/", response_model=BookScanResponse)
async def scan_image(
    file: UploadFile = File(...)
):

    metadata = scan_book(file)

    return BookScanResponse(
        title=metadata.get("title", ""),
        authors=metadata.get("authors", []),
        publisher=metadata.get("publisher", ""),
        edition=metadata.get("edition", ""),
        subject=metadata.get("subject", "")
    )