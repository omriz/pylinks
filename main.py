#!/usr/bin/env python3

from fastapi import FastAPI
from fastapi import responses
from fastapi import HTTPException
from pydantic import BaseModel

import golinker
import golinker.inmemory

app = FastAPI()

goLinker = golinker.GoLinker(golinker.inmemory.InMemory())


class Link(BaseModel):
    target: str

main_page =''
with open('static/index.html','r') as f:
    main_page = f.read()

@app.get("/")
async def root():
    return responses.HTMLResponse(main_page)


@app.get("/api/links")
async def get_all_links():
    return goLinker.All()


@app.get("/api/links/{key}")
async def get_link(key: str):
    link = goLinker.Get(key)
    if link:
        return {"url": link}
    raise HTTPException(status_code=404, detail="link %s not found" % key)


@app.post("/api/links/{key}")
async def store_link(key: str, link: Link):
    goLinker.Set(key, link.target)
    return responses.HTMLResponse()


@app.get("/go/{key}")
async def redirect(key: str):
    link = goLinker.Get(key)
    if link:
        return responses.RedirectResponse(link)
    raise HTTPException(status_code=404, detail="link %s not found" % key)
