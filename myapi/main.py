from fastapi import FastAPI
import asyncio  # Import asyncio for simulating delay
from redis.asyncio.sentinel import Sentinel  # Import Sentinel from redis.asyncio

app = FastAPI()

# Configure Redis Sentinel
sentinel = Sentinel([('redis-sentinel', 26379)], socket_timeout=0.1)
redis_master = sentinel.master_for('mymaster', socket_timeout=0.1)

# Simulate a slow database response
async def simulate_slow_db_response(item_id: int):
    await asyncio.sleep(1)  # Simulate a 0.5-second delay
    return "abc"

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # Use the simulated slow db response
    v = await simulate_slow_db_response(item_id)
    return {"item_id": item_id, "item_value": v}

@app.get("/cached_items/{item_id}")
async def read_cached_item(item_id: int):
    # Check cache first
    cache_key = f"{item_id}"
    cached_item = await redis_master.get(cache_key)
    
    if cached_item:
        v = cached_item.decode('utf-8')
        return {"item_id": item_id, "item_value": v}
    
    v = await simulate_slow_db_response(item_id)
    await redis_master.set(cache_key, v.encode('utf-8'))
    return {"item_id": item_id, "item_value": v}

@app.get("/cache_stampede_items/{item_id}")
async def read_cache_stampede_item(item_id: int):
    # Check cache first
    cache_key = f"{item_id}"
    cached_item = await redis_master.get(cache_key)
    
    if cached_item:
        v = cached_item.decode('utf-8')
        return {"item_id": item_id, "item_value": v}
    
    v = await simulate_slow_db_response(item_id)
    await redis_master.set(cache_key, v.encode('utf-8'))
    return {"item_id": item_id, "item_value": v}

