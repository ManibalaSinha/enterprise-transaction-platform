# db/test_db.py
from app.db.session import SessionLocal
from app.models import Account

db = SessionLocal()

try:
    acc = Account(name="m", email="w@mail.com",balance=1000)
    db.add(acc)
    db.commit()
    db.refresh(acc)

    print(" Inserted:", acc.id, acc.name, acc.balance)

    accounts = db.query(Account).all()
    print(" All accounts:", accounts)

finally:
    db.close()
