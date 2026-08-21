from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import SessionLocal, init_db
from crud import (
    get_tasks,
    create_task,
    delete_task,
    update_task
)

app = FastAPI(title="DevFlow API")

init_db()


class TaskCreate(BaseModel):
    name: str


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "DevFlow API is running!"}


@app.get("/tasks")
def read_tasks():
    db = SessionLocal()

    try:
        tasks = get_tasks(db)

        return {
            "tasks": [
                {
                    "id": task.id,
                    "name": task.name
                }
                for task in tasks
            ]
        }
    finally:
        db.close()


@app.post("/tasks")
def add_task(task: TaskCreate):
    db = SessionLocal()

    try:
        if not task.name.strip():
            raise HTTPException(
                status_code=400,
                detail="Название задачи не может быть пустым!"
            )

        new_task = create_task(db, task.name)

        return {
            "message": "Задача создана",
            "task": {
                "id": new_task.id,
                "name": new_task.name
            }
        }
    finally:
        db.close()


@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    db = SessionLocal()

    try:
        task = delete_task(db, task_id)

        if task is None:
            raise HTTPException(
                status_code=404,
                detail="Такой задачи нет!"
            )

        return {
            "message": "Задача удалена",
            "task": {
                "id": task.id,
                "name": task.name
            }
        }
    finally:
        db.close()


@app.put("/tasks/{task_id}")
def change_task(task_id: int, task: TaskCreate):
    db = SessionLocal()

    try:
        if not task.name.strip():
            raise HTTPException(
                status_code=400,
                detail="Название задачи не может быть пустым!"
            )

        updated_task = update_task(
            db,
            task_id,
            task.name
        )

        if updated_task is None:
            raise HTTPException(
                status_code=404,
                detail="Такой задачи нет!"
            )

        return {
            "message": "Задача изменена",
            "task": {
                "id": updated_task.id,
                "name": updated_task.name
            }
        }
    finally:
        db.close()