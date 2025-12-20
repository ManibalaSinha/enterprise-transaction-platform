from app.db.session import engine, Base
from app.models.user import User  # import all your models here

# This will create all tables defined with Base.metadata
#Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
