import tkinter as tk
from tkinter import messagebox

# Functionality to add tasks
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Functionality to delete selected task
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Functionality to mark a task as completed
def mark_done():
    try:
        task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(task_index)
        listbox_tasks.delete(task_index)
        listbox_tasks.insert(tk.END, task + " (Completed)")
    except:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Setting up the main application window
window = tk.Tk()
window.title("To-Do List App")

# Task entry widget
entry_task = tk.Entry(window, width=35)
entry_task.pack(pady=10)

# Add task button
button_add_task = tk.Button(window, text="Add Task", width=40, command=add_task)
button_add_task.pack(pady=5)

# Listbox to display tasks
listbox_tasks = tk.Listbox(window, width=40, height=10)
listbox_tasks.pack(pady=10)

# Buttons to delete or mark tasks as completed
button_delete_task = tk.Button(window, text="Delete Task", width=40, command=delete_task)
button_delete_task.pack(pady=5)

button_mark_done = tk.Button(window, text="Mark as Completed", width=40, command=mark_done)
button_mark_done.pack(pady=5)

# Running the GUI loop
window.mainloop()
