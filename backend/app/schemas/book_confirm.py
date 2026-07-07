from pydantic import BaseModel


class BookConfirmRequest(BaseModel):
    title: str
    author: str
    isbn: str | None = None
    publisher: str | None = None
    edition: str | None = None
    subject: str | None = None
    branch: str
    semester: int
    description: str | None = None
    image_url: str | None = None