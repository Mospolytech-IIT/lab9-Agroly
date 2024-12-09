from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Post  # импортируем из первого файла

DATABASE_URL = "sqlite:///db.db"

engine = create_engine(DATABASE_URL, echo=True)

Base.metadata.create_all(bind=engine)




