# user등록/조회 관련 api입력 param 및 응답 데이터에 대한 모델

from pydantic import BaseModel
from fastapi import UploadFile,File

class CCTV_INFO(BaseModel):
    cctv_id : str
    location : str
    gps_x : float
    gps_y : float

class CCTV_EVENTS(BaseModel):
    cctv_id : str
    event_time : str
    event_type : str
    event_item : str
    event_description : str
