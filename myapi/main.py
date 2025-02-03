from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/cached_items/{item_id}")
async def read_cached_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

