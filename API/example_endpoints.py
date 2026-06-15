from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Модель данных
class Item(BaseModel):
    name: str
    price: float

# Хранилище
items = {}

# GET - получить все
@app.get("/items")
def get_items():
    return items

# GET - получить один
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return items.get(item_id, {"error": "Not found"})

# POST - создать
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    items[item_id] = item.dict()
    return {"message": "Created", "item": items[item_id]}

# PUT - обновить полностью
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    items[item_id] = item.dict()
    return {"message": "Updated", "item": items[item_id]}

# DELETE - удалить
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"message": "Deleted"}
    return {"error": "Not found"}

# Запуск: uvicorn main:app --reload