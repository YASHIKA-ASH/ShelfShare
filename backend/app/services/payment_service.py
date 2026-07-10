import random

from sqlalchemy.orm import Session

from app.models.payment import Payment


def make_payment(db:Session,data):

    txn="TXN"+str(random.randint(100000,999999))

    payment=Payment(

        user_id=data.user_id,

        rental_id=data.rental_id,

        amount=data.amount,

        payment_method=data.payment_method,

        transaction_id=txn,

        status="Success"

    )

    db.add(payment)

    db.commit()

    db.refresh(payment)

    return {

        "message":"Payment Successful",

        "transaction_id":txn,

        "status":"Success"

    }