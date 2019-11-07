from fastapi import FastAPI
from api import views
import uvicorn

app = FastAPI()

app.include_router(
    views.api, prefix="/api", responses={404: {"description": "Not found"}}
)


@app.get("/")
def root():
    return {"Hello": "world"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
