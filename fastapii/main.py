# from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="template")

conn = MongoClient("mongodb+srv://jainayushh655:SNUr3v9qzn6Fg2wo@cluster1.tqmo3ca.mongodb.net/")

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     docs = conn.notes.notes.find({})
#     newDocs = []
#     for doc in docs:
#         newDocs.append({
#             "id": doc["_id"],
#             "note": doc["note"]
#         })
#     return templates.TemplateResponse(
#         "index.html", {"request": request, "newDocs": newDocs}
#     )


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str| None = None):
#     return {"item_id": item_id, "q": 10}