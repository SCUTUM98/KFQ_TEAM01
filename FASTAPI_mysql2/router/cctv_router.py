from fastapi import APIRouter, Depends, HTTPException
from model.user_model import *
from repository import cctv_repo
from resource.database import get_db
from sqlalchemy.orm import Session
from typing import List


user_router = APIRouter()


@user_router.post("/signup")
def signup(user: cctv_events, db: Session=Depends(get_db)):
    return cctv_repo.insert(db=db, events = user)