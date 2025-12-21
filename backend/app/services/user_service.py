from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User

def create_user(db: Session, name: str, email: str):
    user = User(name=name, email=email)
    db.add(user)

    try:
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        raise ValueError("Email already exists")

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
