from sqlite3 import Date
import string
from fastapi import FastAPI, status

# Initialize app
app = FastAPI()

@app.get("/")
def root():
    return "This my crud api"

@app.post("/crud", status_code=status.HTTP_201_CREATED)
def create_crud_api():
    return "create crud api item"

@app.get("/crud/{name}")
def read_name(name: string):
    return "read crud item with name {name}"


@app.get("/crud/{age}")
def read_age(age: int):
    return "read crud item with age {age}"

@app.get("/crud/{message}")
def read_message(message: string):
    return "read crud item with message {message}"

@app.get("/crud/{createDate}")
def read_date(createDate: Date):
    return "read crud item with Date {createDate}"


@app.get("/crud")
def read_crud_item():
    return "read crud item"
