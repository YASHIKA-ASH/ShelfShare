from pydantic import BaseModel


class WishlistResponse(BaseModel):
    id: int
    user_id: int
    book_id: int

    class Config:
        from_attributes = True