from fastapi import FastAPI
from api.views import api
import uvicorn
from app import CONFIG
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.requests import Request
import os
from markdown import markdown

app = FastAPI()

app.include_router(api, prefix="/api")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", name="index")
def index(request: Request):
    with open(
        os.path.join(CONFIG.BASE_DIR, "README.md"), encoding="utf-8"
    ) as f:
        content = f.read()
    return templates.TemplateResponse(
        "home/index.html",
        {"request": request, "index_content": markdown(content)},
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
