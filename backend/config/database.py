from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv
import os

load_dotenv()

ECHO = False

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=ECHO)

def create_db_and_tables():
  SQLModel.metadata.create_all(engine)