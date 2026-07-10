from typing import Optional
from pydantic import BaseModel

class PaymentCreate(BaseModel):

    user_id: int

    rental_id: Optional[int] = None

    amount: float

    payment_method: str