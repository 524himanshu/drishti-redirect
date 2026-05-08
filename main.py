from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

DASHBOARD = "https://drishti-ai-1.onrender.com"
API_DOCS = "https://drishti-ai-szyx.onrender.com/docs"


@app.get("/")
async def root():
    return HTMLResponse(
        f"""
        <html>
            <head>
                <meta http-equiv="refresh" content="0; url={DASHBOARD}" />
            </head>
            <body>
                Redirecting...
            </body>
        </html>
        """
    )


@app.get("/docs")
async def docs():
    return HTMLResponse(
        f"""
        <html>
            <head>
                <meta http-equiv="refresh" content="0; url={API_DOCS}" />
            </head>
            <body>
                Redirecting...
            </body>
        </html>
        """
    )


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/{path:path}")
async def catch_all(path: str):
    return HTMLResponse(
        f"""
        <html>
            <head>
                <meta http-equiv="refresh" content="0; url={DASHBOARD}" />
            </head>
            <body>
                Redirecting...
            </body>
        </html>
        """
    )