from fastapi import FastAPI
from api import views

app = FastAPI()

app.include_router(
    views.api, prefix="/api", responses={404: {"description": "Not found"}}
)
