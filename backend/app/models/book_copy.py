from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class BookCopy(Base):

    __tablename__ = "book_copies"

    id = Column(Integer, primary_key=True, index=True)

    book_id = Column(
        Integer,
        ForeignKey("books.id"),
        nullable=False
    )

    barcode = Column(
        String(50),
        unique=True,
        nullable=False
    )

    status = Column(
        String(20),
        default="Available"
    )

    rack = Column(
        String(20),
        default="A1"
    )

    condition = Column(
        String(20),
        default="Good"
    )

    book = relationship(
        "Book",
        back_populates="copies"
    )
    rentals = relationship(
    "Rental",
    back_populates="copy"
    )