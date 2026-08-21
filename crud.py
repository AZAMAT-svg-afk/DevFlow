from sqlalchemy.orm import Session

from models import Task


def get_tasks(db: Session):
    return db.query(Task).all()


def create_task(db: Session, name: str):
    task = Task(name=name)

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        return None

    db.delete(task)
    db.commit()

    return task


def update_task(db: Session, task_id: int, name: str):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        return None

    task.name = name
    db.commit()
    db.refresh(task)

    return task