from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from model.cctv_model import *
from repository import cctv_repo
from resource.database import get_db
from sqlalchemy.orm import Session
from typing import List, Union
import os
import json

cctv_router = APIRouter()

UPLOAD_FOLDER = 'C:/Users/USER/Desktop/project/KFQ_TEAM01/API/uploads'

@cctv_router.post("/add_event")
def post(cctv_data: Union[CCTV_EVENTS, str], photo: UploadFile = File(...),
         db: Session=Depends(get_db)):
    try:
        if isinstance(cctv_data, str):
            cctv_event = CCTV_EVENTS(**json.loads(cctv_data))

        
        cctv_repo.insert(db=db, events = cctv_event, photo=photo)
        cctv_repo.save_cctv_image(events = cctv_event, photo=photo)
        return {"result": 0}
    except:
        return {"result": -1}


