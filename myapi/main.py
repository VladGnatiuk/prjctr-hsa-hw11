from fastapi import FastAPI
import asyncio  # Import asyncio for simulating delay

app = FastAPI()

# Simulate a slow database response
async def simulate_slow_db_response(item_id: int, q: str = None):
    await asyncio.sleep(0.5)  # Simulate a 2-second delay
    return {"item_id": item_id, "q": q}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    # Use the simulated slow db response
    return await simulate_slow_db_response(item_id, q)

@app.get("/cached_items/{item_id}")
async def read_cached_item(item_id: int, q: str = None):
    # Use the simulated slow db response
    return await simulate_slow_db_response(item_id, q)

