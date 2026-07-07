from pydantic import BaseModel


class ScanResponse(BaseModel):
    title: str
    authors: list[str]
    publisher: str
    edition: str
    subject: str