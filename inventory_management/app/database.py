from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://sit722_part3_7xjc_user:c5pz0A5t53ODkjePvHQ4c5JpnxukHAKR@dpg-crcbh9dsvqrc73cht100-a.oregon-postgres.render.com/sit722_part3_7xjc" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
