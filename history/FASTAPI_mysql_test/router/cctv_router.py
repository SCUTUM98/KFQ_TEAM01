from fastapi import APIRouter, HTTPException, Depends
from mysql.connector import connect, Error
from pydantic import BaseModel
from typing import Dict

class cctv_events(BaseModel):
    cctv_id: str
    event_item: str
    event_time: str
    event_type: str
    event_description: str

cctv_router = APIRouter()

# MySQL 연결 설정
def get_db_connection():
    return connect(
        host="localhost",
        user="root",
        password="tiger",  # MySQL 컨테이너 실행 시 설정한 비밀번호
        database="cctv_db"       # MySQL 컨테이너 실행 시 설정한 데이터베이스 이름
    )

@cctv_router.post("/records")
async def records(record: cctv_events):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        insert_query = "INSERT INTO cctv_events (cctv_id, event_item, event_time, event_type, event_description) VALUES (%s, %s, %s, %s, %s)"
        insert_values = (record.cctv_id, record.event_item, record.event_time, record.event_type, record.event_description)

        cursor.execute(insert_query, insert_values)
        connection.commit()

        return {"message": "record added successfully"}

    except Error as e:
        raise HTTPException(status_code=500, detail="Database error")

    finally:
        cursor.close()
        connection.close()

# 나머지 라우팅 코드와 함께 추가








# from fastapi import APIRouter, Depends, HTTPException
# from pydantic import BaseModel, ValidationError
# from typing import List, Dict,Optional,Union

# #cctv 기본정보
# class cctv_info(BaseModel):
#     cctv_id : int
#     address : str
#     gps_xy : str
#     cctv_status : str #카메라 고장여부

# #cctv에 잡힌 이벤트
# class cctv_events(BaseModel):
#     cctv_id : int
#     event_time : str
#     event_type : str
#     evnt_description : str

# # 데이터를 저장할 임시 딕셔너리
# cctvs_db: Dict[int, cctv_events] = {}

# record_id = 1

# cctv_router = APIRouter()

# @cctv_router.post("/records")
# async def records(record: cctv_events):
#     global record_id
#     cctvs_db[record_id] = record
#     record_id += 1
#     return {"message": "record added successfully"}

# @cctv_router.get("/records", response_model=cctv_events)
# async def get_records():
#     return cctvs_db

# @cctv_router.get("/records/{record_id}", response_model=cctv_events)
# async def get_record(record_id: int):
#     if record_id in cctvs_db:
#         return cctvs_db[record_id]
#     else:
#         raise HTTPException(status_code=404, detail="record not found")
