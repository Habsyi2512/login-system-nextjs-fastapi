from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import Session, select
from ..models.user import User, UserCreate
from ..utils.password import verify_password, get_password_hash
from ..config.security import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from ..config.database import engine
from datetime import timedelta
import logging

logger = logging.getLogger(__name__)

router = APIRouter()
oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
  with Session(engine) as session:
    user = session.exec(select(User).where(User.email == form_data.username)).first()

    if not user or not verify_password(form_data.password, user.hashed_password):
      logger.warning(f"Attempted registration with existing email: {user.email}")
      raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect email or password",
        headers={"WWW-Authenticate": "Bearer"}
      )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub":user.email}, expires_delta=access_token_expires)

    logger.info(f"New user registered: {user.email}")
    return {"access_token": access_token, "token_type": "bearer"}
  
@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate):
  with Session(engine) as session:
    existing_user = session.exec(select(User).where(User.email == user.email)).first()

    if existing_user:
      raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Email already registered"
      )
    
    # Create a new user
    hashed_password = get_password_hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password, full_name=user.full_name)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"message":"User created successfully"}