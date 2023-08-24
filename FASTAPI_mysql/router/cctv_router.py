from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from model.user_model import *
from repository import cctv_repo
from resource.database import get_db
from sqlalchemy.orm import Session
from typing import List
import os
import shutil

user_router = APIRouter()

# 새로운 코드 추가##############################

# 업로드된 jpg 파일을 저장할 디렉토리 경로
upload_dir = 'C:/workspace/Final_project/KFQ_TEAM01/fastAPI_mysql/image_store'  #상세 경로 수정해주세요

@user_router.post("/signup")
def signup(user: CCTV_EVENTS, db: Session = Depends(get_db), file: UploadFile = File(...)):
    # 데이터베이스에 사용자 정보 등록
    cctv_repo.insert(db=db, events=user)

    # post 되는 파일명 생성
    cctv_id = user.cctv_id
    event_time = user.event_time
    event_type = user.event_type

    # 파일 이름에 사용 가능한 문자로 변환
    sanitized_event_time = event_time.replace(':', '').replace(' ', '_')
    new_filename = f"{cctv_id}_{sanitized_event_time}_{event_type}"
    
    # 파일 저장
    file_path = os.path.join(upload_dir, new_filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    
    return {"message": "User signed up successfully and file uploaded."}

# 기존 코드 ######################################
# @user_router.post("/signup")
# def signup(user: CCTV_EVENTS,  db: Session = Depends(get_db)):
#     return cctv_repo.insert(db=db, events = user)