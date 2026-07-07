from sqlalchemy.orm import Session

from app.models.reservation import Reservation


def reserve_book(db: Session, data):

    last = db.query(Reservation).filter(
        Reservation.book_id == data.book_id
    ).order_by(
        Reservation.queue_position.desc()
    ).first()

    if last:
        position = last.queue_position + 1
    else:
        position = 1

    reservation = Reservation(
        user_id=data.user_id,
        book_id=data.book_id,
        queue_position=position,
        status="Waiting"
    )

    db.add(reservation)
    db.commit()
    db.refresh(reservation)

    return reservation