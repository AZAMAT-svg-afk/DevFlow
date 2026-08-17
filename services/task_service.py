def create_task(tasks, save_tasks):
    task = input("Название задачи: ")
    tasks.append(task)
    save_tasks()
    print("Задача создана:", task)

def show_tasks(tasks):
    print("Ваши задачи:")

    if not tasks:
        print("Задач пока нет.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def search_task(tasks):
    search = input("Введите слово для поиска: ")

    found = False

    for task in tasks:
        if search.lower() in task.lower():
            print("Найдена задача:", task)
            found = True

    if not found:
        print("Задача не найдена.")

def get_task_number(tasks, action):
    try:
        number = int(input(f"Введите номер задачи для {action}: "))

        if number < 1 or number > len(tasks):
            print("Такой задачи нет!")
            return None

        return number - 1

    except ValueError:
        print("Нужно ввести число!")
        return None
    
def delete_task(tasks, save_tasks):
    show_tasks(tasks)

    if not tasks:
        return

    index = get_task_number(tasks, "удаления")

    if index is None:
        return

    deleted_task = tasks.pop(index)
    save_tasks()

    print("Задача удалена:", deleted_task)
    
def update_task(tasks, save_tasks):
    show_tasks(tasks)

    if not tasks:
        return

    index = get_task_number(tasks, "изменения")

    if index is None:
        return

    new_task = input("Новое название: ")

    if not new_task.strip():
        print("Название не может быть пустым!")
        return

    tasks[index] = new_task
    save_tasks()

    print("Задача изменена:", new_task)