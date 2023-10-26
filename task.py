tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def mark_task_as_completed(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
    else:
        print("Invalid task index.")

def list_tasks():
    if tasks:
        print("Task List:")
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{index + 1}. {task['task']} ({status})")
    else:
        print("Task list is empty.")

while True:
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. List Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        add_task(task)
    elif choice == "2":
        task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
        mark_task_as_completed(task_index)
    elif choice == "3":
        list_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please select a valid option.")
