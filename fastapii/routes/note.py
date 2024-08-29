from fastapi import APIRouter
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from models.note import Note
from fastapi.templating import Jinja2Templates

from config.db import  conn
from schema.note import  noteEntity, notesEntity

note = APIRouter()
templates = Jinja2Templates(directory="template")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "title": doc["title"],
            "desc": doc["desc"],
            "important": doc["important"]
        })
    return templates.TemplateResponse(
        "index.html", {"request": request, "newDocs": newDocs}
    )

@note.post("/", response_class=HTMLResponse)
async def create_item(request: Request):
    form = await request.form()
    note = conn.notes.notes.insert_one(dict(form))
    return {"Success": True}
    pass