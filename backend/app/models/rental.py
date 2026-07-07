from sqlalchemy import (
    Column,
    Integer,
    Date,
    String,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database import Base


class Rental(Base):

    __tablename__ = "rentals"

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

    user = relationship(
        "User",
        back_populates="rentals"
    )


    issue_date = Column(Date)

    due_date = Column(Date)

    return_date = Column(Date)

    status = Column(String(20))

    rating = Column(Integer)

    fine = Column(
    Integer,
    default=0
)
    
    copy_id = Column(
    Integer,
    ForeignKey("book_copies.id"),
    nullable=False
)

    copy = relationship(
    "BookCopy",
    back_populates="rentals"
)   