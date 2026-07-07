from pydantic import BaseModel


class BookSummary(BaseModel):

    id: int

    title: str

    author: str

    subject: str

    publisher: str

    class Config:
        from_attributes = True