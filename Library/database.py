from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#database url
SQLALCHEMY_DATABASE_URL = 'sqlite:///./book.db'

#creating engine at the database url
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})

#creating a local session
SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base = declarative_base()

#method to get current session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()