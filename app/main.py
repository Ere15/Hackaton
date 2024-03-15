from fastapi import FastAPI
from app.api.endpoints.api import router as api_router
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(api_router)

app.mount("/static", StaticFiles(directory="app/Hakaton/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_html():
    with open("app\Hakaton\Login.html", "r") as file:
        html_content = file.read()
    return html_content

@app.get("/emp", response_class=HTMLResponse)
async def get_page1():
    with open("app\Hakaton\employee.html", "r") as file:
        html_content = file.read()
    return html_content

@app.get("/req", response_class=HTMLResponse)
async def get_page2():
    with open("app\Hakaton\request_details.html", "r") as file:
        html_content = file.read()
    return html_content