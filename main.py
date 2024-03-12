from fastapi import FastAPI, Query, File, UploadFile
from typing_extensions import Annotated
from typing import Union
from fastapi.responses import ORJSONResponse

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

@app.get("/validations/")
async def validation_exmaple(
    q: Annotated[
        Union[str, None],
        Query(min_length=3, max_length=50, regex="\d+")
    ] = "mambo jambo"
):
    result = {"q": q}
    if q:
        result.update({"q": q})
    return result

@app.post("/files")
async def create_file(file: Annotated[bytes, File()]):
    print("test")
    return {"file_size": len(file)}

@app.post("/uploadfile", response_class=ORJSONResponse)
async def create_upload_file(file: UploadFile):
    return ORJSONResponse([{"filename": file.filename}])
