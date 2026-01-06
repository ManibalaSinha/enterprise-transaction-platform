import time
from sqlalchemy.orm import Session
from app.models.payment import Payment
from app.models.payment_attempt import PaymentAttempt
from app.models.idempotency_key import IdempotencyKey
from app.utils.logger import logger # structured logging

MAX_RETRIES = 3
BACKOFF = [1,2,4] #sec
def create_payment(db: Session, user_id: int, amount: float, currency: str, idempotency_key: str):
   #checking idempotency
   existing_key= db.query(idempotency_key).filter_by(key=idempotency_key).first()
   if existing_key:
      payment = db.query(payment).filter_by(id=existing_key.payment_id).first()
      attempts= len(payment.attempts)
      return payment, attempts
   
   #creating new payment
   payment = Payment(user_id=user_id, amount=amount, currency=currency)
   db.add(payment)
   db.commit()
   db.refresh(payment)

   #save idempotency key
   db_key = IdempotencyKey(key=idempotency_key, payment_id=payment.id)
   db.add(db_key)
   db.commit()

   #retry logic
   for attempt_no in range(1, MAX_RETRIES + 1):
      try:
         #simulate payment processing
         process_payment(payment)
         payment.status="Success"
         db.commit()
         logger.info(f"Payment {payment.id} succeded on attempt {attempt_no}")
         return payment, attempt_no
      except Exception as e:
         attempt = PaymentAttempt(payment_id = payment.id, attempt_no=attempt_no,status = "Failed", error_message=str(e))
         db.add(attempt)
         db.commit()
         logger.warning(f"payment {payment.id} failed attempt {attempt_no}: {e}")

         if attempt_no < MAX_RETRIES:
            time.sleep(BACKOFF[attempt_no - 1])
         else:
            payment.status = "Failed"
            db.commit()
            logger.error(f"Payment {payment.id} failed after {MAX_RETRIES} attempts")
            return payment,attempt_no
def process_payment(payment: Payment):
   # Simulate payment processing (replace with real API call).
   if payment.amount %2 == 0: #Simulate transient error
      raise Exception("Transient payment error")
   return True
            
