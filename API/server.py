from fastapi import FastAPI
import logging, uvicorn
logging.basicConfig(level=logging.INFO)
app = FastAPI()

@app.get("/data")
def get_data():
    logging.info("GET /data")
    return {"message": "Hello, World!"}

uvicorn.run(app, host="0.0.0.0", port=8001)