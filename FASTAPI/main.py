from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

# API Server로 받아오고자 하는 데이터 형태
# description ?? => 422 error
class Item(BaseModel):
    camera_name : str 
    time : str
    xmin : float
    ymin : float
    xmax : float
    ymax : float
    confidence : float
    mclass : int
    name : str

@app.get("/")
def 환영합니다():
  return 'Welcome!'

@app.put("/items")
async def update_item(item: Item):
    results = {"item": item}
    return results