from typing import List, Dict,Optional,Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    camera_name: str
    time: str
    xmin: Optional[float] = None
    ymin: Optional[float] = None
    xmax: Optional[float] = None
    ymax: Optional[float] = None
    confidence: Optional[float] = None
    type_class: int
    name: str
    action : str

# 데이터를 저장할 임시 딕셔너리
items_db: Dict[int, Item] = {}

item_id = 1

@app.put("/items")
async def update_item(item: Item):
    global item_id
    items_db[item_id] = item
    item_id += 1
    return {"message": "Item added successfully"}

@app.get("/items")
async def get_items():
    return items_db

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id in items_db:
        return items_db[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")
