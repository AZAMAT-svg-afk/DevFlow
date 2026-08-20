import json

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

from services.task_service import (
    create_task,
    show_tasks,
    search_task,
    delete_task,
    update_task
)

app = FastAPI(title= "DevFlow API" )
class Task(BaseModel):
    name: str

with open("tasks.json", "r", encoding="utf-8") as file:
    tasks = json.load(file)

def save_tasks():
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)
        
@app.get("/")
def root():
    return {"message": "DevFlow API is running!"}

@app.get("/tasks")
def get_tasks():
    return {"tasks": show_tasks(tasks)}

@app.post("/tasks")
def add_task(task: Task):
    created_task = create_task(tasks, save_tasks, task.name)

    return {
        "message": "Задача создана",
        "task": created_task
    }
    
@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    deleted_task = delete_task(tasks, save_tasks, task_id)

    if deleted_task is None:
        raise HTTPException(
            status_code=404,
            detail="Такой задачи нет!"
        )

    return {
        "message": "Задача удалена",
        "task": deleted_task
    }
    
@app.put("/tasks/{task_id}")
def change_task(task_id: int, task: Task):
    updated_task = update_task(
        tasks,
        save_tasks,
        task_id,
        task.name
    )

    if updated_task is None:
        raise HTTPException(
            status_code=404,
            detail="Такой задачи нет или название пустое!"
        )

    return {
        "message": "Задача изменена",
        "task": updated_task
    }
    
@app.get("/tasks/search")
def search_tasks(keyword: str = Query(...)):
    found_tasks = search_task(tasks, keyword)

    return {
        "results": found_tasks
    }