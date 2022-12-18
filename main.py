#!/usr/bin/env python3

from fastapi import FastAPI
from fastapi import responses

import golinker

app = FastAPI()

goLinker = golinker.GoLinker()

@app.get("/")
async def root():
    c = r'''
<!DOCTYPE html>
<html lang="en-us">
<header>
<title>Testing Page</title>
</header>

<body>
<h1>Header</h1>
<p>Paragraph</p>
</body>
</html>
'''
    return responses.HTMLResponse(c)

@app.get("/api")
async def api():
    return {"message": "API message"}