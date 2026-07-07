from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class Reservation(Base):

    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    book_id = Column(
        Integer,
        ForeignKey("books.id"),
        nullable=False
    )

    queue_position = Column(
        Integer,
        nullable=False
    )

    status = Column(
        String(20),
        default="Waiting"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user = relationship(
        "User",
        back_populates="reservations"
    )

    book = relationship(
        "Book",
        back_populates="reservations"
    )