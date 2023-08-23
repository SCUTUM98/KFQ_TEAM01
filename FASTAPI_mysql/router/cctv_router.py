from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from model.user_model import *
from repository import cctv_repo
from resource.database import get_db
from sqlalchemy.orm import Session
from typing import List
import os
import shutil

user_router = APIRouter()

#새로운 코드 추가##############################

# 업로드된 jpg 파일을 저장할 디렉토리 경로
# upload_dir = 'KFQ_TEAM01/DB/image_store'  #상세 경로 수정해주세요

# # 업로드된 파일을 저장하기 위한 디렉토리 생성
# if not os.path.exists(upload_dir):
#     os.makedirs(upload_dir)

# @user_router.post("/signup")
# def signup_with_image(
#     user: CCTV_EVENTS,  # cctv_events 모듈의 적절한 클래스로 수정해주세요
#     image: UploadFile = File(...),
#     db: Session = Depends(get_db)
# ):
#     try:
#         # 사용자 정보 데이터베이스에 추가
#         created_event = cctv_repo.insert(db=db, events=user)
        
#         # 업로드된 이미지를 저장
#         image_path = os.path.join(upload_dir, image.filename)
#         with open(image_path, "wb") as f:
#             shutil.copyfileobj(image.file, f)
        
#         return {"message": "User and image uploaded successfully"}
#     except Exception as e:
#         return {"message": "An error occurred", "error": str(e)}


# 기존 코드 ######################################
@user_router.post("/signup")
def signup(user: CCTV_EVENTS,  db: Session = Depends(get_db)):
    return cctv_repo.insert(db=db, events = user)

