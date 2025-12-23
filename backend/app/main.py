from fastapi import Depends, FastAPI
from app.api.users import router
from app.db.session import SessionLocal
from app.models.user import User
from app.db.session import engine
from app.models import Base
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.api import users

app = FastAPI(
    title="Enterprise Transaction Processing Platform",
    version="1.0.0"
)

app.include_router(users.router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    print(" Database tables ensured")
    
@app.get("/health")
def health_check():
    return {"status": "ok"}
