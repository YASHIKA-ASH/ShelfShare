from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.schemas.payment import PaymentCreate

from app.services.payment_service import make_payment

router=APIRouter(

    prefix="/payments",

    tags=["Payments"]

)

@router.post("/")

def pay(

    payment:PaymentCreate,

    db:Session=Depends(get_db)

):

    return make_payment(db,payment)