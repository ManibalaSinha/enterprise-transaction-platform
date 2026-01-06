import logging
from app.db.session import SessionLocal

logger = logging.getLogger(__name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"DB session rollback due to {e}")
        db.rollback()
        raise
    finally:
        db.close()
