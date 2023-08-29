from model.cctv_model import *
from resource.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Float,Text
from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException
import os
from fastapi import FastAPI, File, UploadFile, HTTPException
import json
from typing import Union

class INFO(Base):
    __tablename__ = "cctv_info"

    cctv_id = Column(String, primary_key=True)
    location = Column(Text)
    gps_x = Column(Float)
    gps_y = Column(Float)


class EVENTS(Base):
    __tablename__ = "cctv_events"

    cctv_id = Column(String, primary_key=True)
    event_time = Column(String, primary_key=True)
    event_type = Column(String, primary_key=True)
    event_item = Column(String)
    event_description = Column(String)

UPLOAD_FOLDER = 'C:/workspace/Final_project/KFQ_TEAM01/FASTAPI_mysql/uploads'

def insert(db: Session, events: CCTV_EVENTS, photo: UploadFile = File(...))-> EVENTS:

    try:
        record = EVENTS(
            cctv_id = events.cctv_id,
            event_time = events.event_time,
            event_type = events.event_type,
            event_item = events.event_item,
            event_description = events.event_description
        )

        db.add(record)
        db.commit()


    except Exception as e:
        db.rollback()
        print(e)
        raise Exception(status_code=500, detail='Database Error:(')
    
def save_cctv_image(events: CCTV_EVENTS, photo: UploadFile = File(...)):

    tv_id = events.cctv_id
    tv_time_1=events.event_time.replace(' ','')
    tv_time_2=tv_time_1.replace("-","_")
    tv_time=tv_time_2.replace(":","")
    tv_type=events.event_type
    photo_path = os.path.join(UPLOAD_FOLDER,f"{tv_id}{tv_time}{tv_type}.jpg")

    with open(photo_path, "wb") as buffer:
        buffer.write(photo.file.read())

    return {"photo_path": photo_path}
