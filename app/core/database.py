import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = sa.create_engine("sqlite:///example.db", echo=True)

session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = session() 
    try:
        yield db
    finally:
        db.close()
