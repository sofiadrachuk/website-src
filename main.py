from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Example route
@app.get("/api/hello")
async def read_hello():
    return {"message": "Hello, World!"}

# Model for POST data
class Item(BaseModel):
    id: int
    name: str

@app.post("/api/data")
async def post_data(item: Item):
    return {"received": item}

@app.get("/api/items")
async def get_items():
    items = [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
    ]
    return items
