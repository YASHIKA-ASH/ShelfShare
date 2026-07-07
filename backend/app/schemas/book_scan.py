from pydantic import BaseModel

class BookScanResponse(BaseModel):
    title: str
    authors: list[str]
    publisher: str
    edition: str
    subject: str