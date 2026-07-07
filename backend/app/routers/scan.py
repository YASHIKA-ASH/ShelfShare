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
        title=metadata["title"],
        authors=metadata["authors"],
        publisher=metadata["publisher"],
        edition=metadata["edition"],
        subject=metadata["subject"]
    )