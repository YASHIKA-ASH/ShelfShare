from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    password_hash = Column(String(255), nullable=False)

    phone = Column(String(15), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    books = relationship(
    "Book",
    back_populates="owner"
)
    rentals = relationship(
    "Rental",
    back_populates="user"
)
    wishlist = relationship(
    "Wishlist",
    back_populates="user"
)
    role = Column(
    String(20),
    default="Student"
)   
    reservations = relationship(
    "Reservation",
    back_populates="user"
)