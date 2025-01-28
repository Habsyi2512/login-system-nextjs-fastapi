from fastapi import FastAPI, Depends, HTTPException, status
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from . import User
from .config.database import engine, create_db_and_tables

from .routes.auth import router as auth_router

@asynccontextmanager
async def lifespan(app:FastAPI):
  create_db_and_tables()
  yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://localhost:3000"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.delete("/delete_all_users", status_code=status.HTTP_200_OK)
async def delete_all_users():
  with Session(engine) as session:
    users = session.exec(select(User)).all()
    for user in users:
      session.delete(user)
    session.commit()
    return {"message": "All users deleted successfully"}

app.include_router(auth_router, prefix="/auth")
