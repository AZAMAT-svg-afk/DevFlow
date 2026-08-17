import json
from services.task_service import create_task
from services.task_service import create_task, show_tasks
from services.task_service import create_task, show_tasks, search_task
from services.task_service import (
    create_task,
    show_tasks,
    search_task,
    delete_task
    
)
from services.task_service import (
    create_task,
    show_tasks,
    search_task,
    delete_task,
    update_task
)
with open("tasks.json", "r", encoding="utf-8") as file:
    tasks = json.load(file)
def save_tasks():
    with open("tasks.json", "w", encoding ="utf-8") as file: 
       json.dump(tasks, file, ensure_ascii=False, indent=4)

while True:
 print("======================")
 print("      DEVFLOW   ")
 print("======================")
 print("1 Создать Задачу")
 print("2 Просмотреть Задачи")
 print("3 Найти Задачу")
 print("4 Удалить Задачу")
 print("5 Изменить Задачу")
 print("6 Выход")
 choice = input("Выберите действие: ")
 if choice == "1":
    create_task(tasks, save_tasks)

 elif choice == "2":

   print("Просмотр задач")
   show_tasks(tasks)
  
 elif choice == "3":
     search_task(tasks)
     
 elif choice == "4":
    delete_task(tasks, save_tasks)

 elif choice == "5":
    update_task(tasks, save_tasks)
 elif choice == "6":
    print("Выход")
    break
 else:
  print("Неверный выбор") 