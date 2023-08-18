from model.user_model import *
from resource.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException


class User(Base):
    __tablename__ = "cctv_events"

    cctv_id = Column(String, primary_key=True)
    event_time = Column(String, primary_key=True)
    event_type = Column(String, primary_key=True)
    event_item = Column(String)
    event_description = Column(String)
    
def insert(db: Session, events: cctv_events)-> User:
    try:
        record = User(
            cctv_id = events.cctv_id,
            event_time = events.event_time,
            event_type = events.event_type,
            event_item = events.event_item,
            event_description = events.event_description
        )
        db.add(record)
        db.commit()
        
        return record
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail='Database Error:(')