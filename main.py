from fastapi import FastAPI
from typing import Union

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from src.Models.User import User

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

@app.post("/users")
async def create_user(user: User):
    return user
