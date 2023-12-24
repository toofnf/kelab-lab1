from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator
import random

app = FastAPI()

Instrumentator().instrument(app).expose(app)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    d = random.choice([0, 1, 1, 1])
    if d == 0:
        raise HTTPException(status_code=500, detail="Ups.. random works here")
    return {"item_id": item_id, "q": q}
