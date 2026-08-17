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
        print(index, task)

def search_task(tasks):
    search = input("Введите слово для поиска: ")

    found = False

    for task in tasks:
        if search.lower() in task.lower():
            print("Найдена задача:", task)
            found = True

    if not found:
        print("Задача не найдена.")

def delete_task(tasks, save_tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Введите номер задачи для удаления: "))

        if number < 1 or number > len(tasks):
            print("Такой задачи нет!")
            return

        deleted_task = tasks.pop(number - 1)
        save_tasks()

        print("Задача удалена:", deleted_task)

    except ValueError:
        print("Нужно ввести число!")

def update_task(tasks, save_tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Введите номер задачи для изменения: "))

        if number < 1 or number > len(tasks):
            print("Такой задачи нет!")
            return

        new_task = input("Новое название: ")

        if not new_task.strip():
            print("Название не может быть пустым!")
            return

        tasks[number - 1] = new_task
        save_tasks()

        print("Задача изменена:", new_task)

    except ValueError:
        print("Нужно ввести число!")