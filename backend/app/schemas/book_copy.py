from pydantic import BaseModel


class BookCopyCreate(BaseModel):
    number_of_copies: int
    rack: str


class BookCopyResponse(BaseModel):
    id: int
    barcode: str
    rack: str
    status: str
    condition: str

    class Config:
        from_attributes = True