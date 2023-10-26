# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' has been added to the to-do list.")

# Function to view all tasks in the list
def view_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

# Function to remove a task from the list
def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' has been removed from the to-do list.")
    else:
        print("Invalid task index. Please enter a valid index.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        task_index = int(input("Enter the index of the task to remove: "))
        remove_task(task_index)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
