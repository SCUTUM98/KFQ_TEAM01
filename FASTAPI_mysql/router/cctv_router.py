from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from model.user_model import *
from repository import cctv_repo
from resource.database import get_db
from sqlalchemy.orm import Session

user_router = APIRouter()

@user_router.post("/signup")
def signup(user: CCTV_EVENTS,  db: Session = Depends(get_db)):
    return cctv_repo.insert(db=db, events = user)