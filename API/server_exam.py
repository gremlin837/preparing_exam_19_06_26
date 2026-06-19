from fastapi import FastAPI
import uvicorn
app = FastAPI()
data = []
@app.post("/add")
def add(value):
    data.append(value)
    return {"ok": True}
@app.get("/get")
def get_all():
    return data
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)