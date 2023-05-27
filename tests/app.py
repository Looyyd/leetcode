# requirements: fastapi, uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Hello, World!"}

# This file is named main.py
