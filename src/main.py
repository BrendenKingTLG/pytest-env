import os
from fastapi import FastAPI

x = os.getenv('test', 'default')

app = FastAPI()

@app.get("/")
async def root():
    return {"var": x}