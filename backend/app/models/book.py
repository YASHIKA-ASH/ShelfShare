from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class Book(Base):

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(200), nullable=False)

    author = Column(String(100), nullable=False)

    isbn = Column(String(20), unique=True)

    publisher = Column(String(100))

    edition = Column(String(50))

    subject = Column(String(100))

    branch = Column(String(50))

    semester = Column(Integer)

    description = Column(Text)

    image_url = Column(String(255))

    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    owner = relationship(
        "User",
        back_populates="books"
    )


    wishlist = relationship(
        "Wishlist",
        back_populates="book"
    )

    copies = relationship(
        "BookCopy",
        back_populates="book",
        cascade="all, delete-orphan"
    )
    reservations = relationship(
    "Reservation",
    back_populates="book"
    )