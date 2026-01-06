from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import PaymentCreate, PaymentStatus
from app.services.payment_service import create_payment
from app.utils.db import get_db
#from app.schemas.payment_create import PaymentCreate
#from app.schemas.payment_status import PaymentStatus
from app.schemas.payments import PaymentCreate, PaymentStatus

router = APIRouter()

@router.post("/initiate-payment", response_model=PaymentStatus)
def initiate_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    result, attempts = create_payment(
        db,
        payment.user_id,
        payment.amount,
        payment.currency,
        payment.idempotency_key
    )
    return PaymentStatus(payment_id=result.id, status=result.status, attempts=attempts)
