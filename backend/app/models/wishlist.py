from sqlalchemy import (
    Column,
    Integer,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database import Base


class Wishlist(Base):

    __tablename__ = "wishlist"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

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

    user = relationship(
        "User",
        back_populates="wishlist"
    )

    book = relationship(
        "Book",
        back_populates="wishlist"
    )