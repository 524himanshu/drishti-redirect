from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse(url="https://drishti-ai-1.onrender.com")

@app.get("/docs")
async def docs():
    return RedirectResponse(url="https://drishti-ai-szyx.onrender.com/docs")

@app.get("/{path:path}")
async def catch_all(path: str):
    return RedirectResponse(url="https://drishti-ai-1.onrender.com")