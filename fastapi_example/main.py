from typing import Union
from fastapi import FastAPI
import asyncio

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):

    await asyncio.sleep(2)
    if item_id == 0:
        # This is to prove that an exception will not crash the server
        raise Exception('Exception on purpse if item_id is 0')
    
    return {"item_id": item_id, "q": q}
