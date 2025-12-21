from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Account(Base):
    __tablename__ = "accounts"

    acc_id = Column(Integer, primary_key=True, index=True)
    balance = Column(Integer,nullable=False)
