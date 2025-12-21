from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Transaction(Base):
    __tablename__ = "transactions"

    txn_id = Column(Integer, primary_key=True, index=True)
    acc_id = Column(Integer, foreign_key=True, index=True)
    amount = Column(Integer,nullable=False)

