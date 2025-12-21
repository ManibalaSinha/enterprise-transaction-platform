from fastapi import FastAPI
from app.api import users  # your router
from app.db.session import SessionLocal
from app.models.user import User

app = FastAPI(
    title="Enterprise Transaction Processing Platform",
    version="1.0.0"
)

app.include_router(users.router)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_event():
    # Add a default user only if not exists
    db = SessionLocal()
    existing = db.query(User).filter_by(email="m@example.com").first()
    if not existing:
        new_user = User(name="M", email="m@example.com")
        db.add(new_user)
        db.commit()
    db.close()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}
