from app.db.base import Base
from app.db.session import engine
from app.models.user import User
from app.models.lead import Lead

def init_db():
    Base.metadata.create_all(bind=engine)