from pydantic import BaseModel


class ReservationCreate(BaseModel):
    user_id: int
    book_id: int


class ReservationResponse(BaseModel):
    id: int
    user_id: int
    book_id: int
    queue_position: int
    status: str

    class Config:
        from_attributes = True