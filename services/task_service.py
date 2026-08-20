def create_task(tasks, save_tasks, task_name):
    tasks.append(task_name)
    save_tasks()

    return task_name


def show_tasks(tasks):
    return tasks


def search_task(tasks, keyword):
    found_tasks = []

    for task in tasks:
        if keyword.lower() in task.lower():
            found_tasks.append(task)

    return found_tasks


def delete_task(tasks, save_tasks, task_id):
    if task_id < 1 or task_id > len(tasks):
        return None

    deleted_task = tasks.pop(task_id - 1)
    save_tasks()

    return deleted_task


def update_task(tasks, save_tasks, task_id, new_task):
    if task_id < 1 or task_id > len(tasks):
        return None

    if not new_task.strip():
        return None

    tasks[task_id - 1] = new_task
    save_tasks()

    return new_task