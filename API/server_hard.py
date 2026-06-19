from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging, uvicorn

logging.basicConfig(level=logging.INFO)
app = FastAPI()

# Модель данных
class Item(BaseModel):
    name: str
    price: float

# Хранилище
items: dict[int, Item] = {}


# GET - получить все элементы

@app.get("/items")
def get_items():
    logging.info(f"GET /items")
    return items


# GET - получить один элемент по ID

@app.get("/items/{item_id}")
def get_item(item_id: int):
    logging.info(f"GET /items/{item_id}")
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

# POST - создать новый элемент

@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    logging.info(f"POST /items/{item_id}")
    if item_id in items:
        raise HTTPException(status_code=409, detail="Item already exists")
    items[item_id] = item
    logging.info(f"Created item {item_id}: {item}")
    return {"message": "Created", "item": item}


# PUT - полностью обновить элемент

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    logging.info(f"PUT /items/{item_id}")
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    logging.info(f"Updated item {item_id}: {item}")
    return {"message": "Updated", "item": item}


# DELETE - удалить элемент

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    logging.info(f"DELETE /items/{item_id}")
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    logging.info(f"Deleted item {item_id}")
    return {"message": "Deleted"}