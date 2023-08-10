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
    mlass : int
    name : str

@app.get("/")
def 환영합니다():
  return 'Welcome!'

@app.put("/items/{item_id}")
async def update_item(
    item: Item = Body(
        ...,
        example={
            "camera_name":"DaeyaIntersection",
            "time":"2023-08-07 10:32:20.982046",
            "xmin":105.61141967773438,
            "ymin":350.4307861328125,
            "xmax":142.32504272460938,
            "ymax":377.0431518554688,
            "confidence":0.8104487657546997,
            "mclass":2,
            "name":"car",
        },
    ),
):
    results = {"item": item}
    return results