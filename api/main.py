from typing import Optional
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def reload():
    return {"Hello":"World"}


