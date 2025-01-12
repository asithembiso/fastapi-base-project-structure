from fastapi import FastAPI
from app.api.controllers import items

app = FastAPI()

app.include_router(items.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

