import os
import os.path

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
sqlite_db = 'sqlite:///' + os.path.join(dir_path, ".db", "counter.db") 

#SQLALCHEMY_DATABASE_URL = 'sqlite:///c:\\Users\\rrastik\Documents\\aplikace-programy\\skripty\\python\\fastapi\\freeradius\\freeradius\\app_test\\db_sqlite3'
SQLALCHEMY_DATABASE_URL = sqlite_db

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()