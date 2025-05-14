
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World and welcome to my first API!"}

@app.get("/about")
def about():
    return {"message": "This is a simple API that returns a message."}

@app.get("/third_api")
def third_api():
    return {"message": "This is the third API endpoint."}