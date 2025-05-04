from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.schemas.user_schema import UserSchema
from src.services import user_service

router = APIRouter()

@router.post("/create/")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)