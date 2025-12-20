from fastapi import FastAPI
from app.db.session import SessionLocal
from app.models.user import User
from backend.app.db import session
app = FastAPI(
   title="Enterprise Transaction Processing Platform",
   version="1.0.0"
)
db = SessionLocal()

new_user = User(name="Mani", email="mani@example.com")
db.add(new_user)
db.commit()
db.refresh(new_user)
print(new_user.id, new_user.name)
db.close()

existing = session.query(User).filter_by(email="mani@example.com").first()
if not existing:
    session.add(User(name="Mani", email="mani@example.com"))
    session.commit()

@app.get("health")
async def health_check():
   return {"status":"ok"}