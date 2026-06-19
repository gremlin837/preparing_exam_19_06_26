from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

items: dict[int, Item] = {}

def get_item_or_404(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

ItemDep = Annotated[Item, Depends(get_item_or_404)]

@app.get("/items")
def get_all() -> dict[int, Item]:
    return items

@app.get("/items/{item_id}")
def get_one(item: ItemDep) -> Item:
    return item

@app.post("/items/{item_id}", status_code=201)
def create(item_id: int, item: Item) -> Item:
    if item_id in items:
        raise HTTPException(status_code=409, detail="Item already exists")
    items[item_id] = item
    return item

@app.put("/items/{item_id}")
def update(item_id: int, new_item: Item, old_item: ItemDep) -> Item:
    items[item_id] = new_item
    return new_item

@app.delete("/items/{item_id}", status_code=204)
def delete(item_id: int, item: ItemDep):
    del items[item_id]
    # 204 No Content, тело не возвращается