from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
from typing import Optional
from pydantic import EmailStr, field_validator
import re

class User(SQLModel, table=True):
  __tablename__ = "users"

  id: Optional[int] = Field(default=None, primary_key=True)
  email: str = Field(unique=True, index=True)
  hashed_password: str
  full_name: str
  is_active:bool = True
  create_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class UserCreate(SQLModel):
  email: EmailStr
  password: str = Field(min_length=8, max_length=128)
  full_name: str = Field(min_length=3, max_length=128)

  @field_validator("password", mode="before")
  @classmethod
  def validate_email(cls, value: str)-> str:
    if len(value) < 8 or len(value) > 128:
      raise ValueError("Password must be between 8 and 128 characters long.")
    if not re.search(r"[A-Z]", value):
      raise ValueError("Password must contain at least one uppercase letter.")
    if not re.search(r"\d", value):
      raise ValueError("Password must containt at least one number.")
    return value
    
  @field_validator("full_name", mode="before")
  @classmethod
  def validate_full_name(cls, value:str)->str:
    if len(value) < 3 or len(value) > 128:
      raise ValueError("Full name must be between 3 and 128 characters long.")
    return value

