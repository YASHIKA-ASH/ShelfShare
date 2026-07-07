from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    author: str
    isbn: str
    publisher: str
    edition: str
    subject: str
    branch: str
    semester: int
    description: str
    image_url: str


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    isbn: str
    publisher: str
    edition: str
    subject: str
    branch: str
    semester: int
    description: str
    image_url: str
    owner_id: int

    class Config:
        from_attributes = True