from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

# description ?? => 422error
class Item(BaseModel):
    camera_name : str # 필수 속성으로 갖고 str인지 검사
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