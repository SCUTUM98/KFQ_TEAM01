from fastapi import APIRouter, Depends, HTTPException, File
from model.user_model import *
from repository import cctv_repo
from resource.database import get_db
from sqlalchemy.orm import Session
from typing import List
import os


user_router = APIRouter()

# 업로드된 jpg 파일을 저장할 디렉토리 경로
upload_dir = 'uploads'

# 업로드된 파일을 저장하기 위한 디렉토리 생성
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

@user_router.post("/signup")
def signup(user: cctv_events,  db: Session = Depends(get_db)):
    return cctv_repo.insert(db=db, events = user)

