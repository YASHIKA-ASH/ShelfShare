from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime

class Payment(Base):

    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    rental_id = Column(
    Integer,
    ForeignKey("rentals.id"),
    nullable=True
)

    amount = Column(Float)

    payment_method = Column(String(30))

    transaction_id = Column(String(50), unique=True)

    status = Column(String(20), default="Success")

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now())