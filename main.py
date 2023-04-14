from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/url-query/")
async def url_query(
    id: Union[int, None] = None,
    name: Union[str, None] = None
):
    result = {"id": 1, "name": "python"}
    if id:
        result.update({"id":id})
    if name:
        result.update({"name":name})
    
    return result