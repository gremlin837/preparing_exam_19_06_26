from fastapi import FastAPI
app = FastAPI()
items = {}
@app.get("/items")
def get(): return items
@app.get("/items/{i}")
def get(i): return items.get(i)
@app.post("/items/{i}")
def post(i, item: dict): items[i] = item; return item
...