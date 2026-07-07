from pydantic import BaseModel
from datetime import date


class RentalCreate(BaseModel):
    user_id: int
    book_id: int
    issue_date: date
    due_date: date


class RatingRequest(BaseModel):
    rental_id: int
    rating: int


class RentalResponse(BaseModel):
    id: int
    user_id: int
    copy_id: int
    issue_date: date
    due_date: date
    return_date: date | None = None
    status: str
    rating: int | None = None
    fine: int

    class Config:
        from_attributes = True