from fastapi import FastAPI
from api.views import api
import uvicorn

app = FastAPI()

app.include_router(api, prefix="/api")


@app.get("/")
def root():
    return {"Hello": "world"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
