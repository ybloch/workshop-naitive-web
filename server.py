from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def root():
    with open("static/index.html", "r") as html_file:
        return html_file.read()


@app.post("/login")
async def login(request: Request):
    data = await request.json()
    print(f"Got {data}")
    return {"message": "Login successful", "data": data}


@app.get("/api/v1/tasks")
async def login():
    mongo_client = MongoClient(
        "localhost", username="admin", password="123123")
    db = mongo_client["bootcamp"]
    tasks = db["tasks"]
    tasks_list = tasks.find({}, {"_id": 0})
    return list(tasks_list)
    # example data
    # return [
    #     {"id": 1, "title": "Task 1", "description": "Task 1 description"},
    #     {"id": 2, "title": "Task 2", "description": "Task 2 description"},
    #     {"id": 3, "title": "Task 3", "description": "Task 3 description"},
    # ]
