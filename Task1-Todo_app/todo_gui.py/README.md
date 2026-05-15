import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")

tasks = []


def add_task():
    task = task_entry.get()

    if task != "":
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")


def delete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
        tasks.pop(selected_task)
    except:
        messagebox.showwarning("Warning", "Please select a task!")


def mark_completed():
    try:
        selected_task = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task)

        task_listbox.delete(selected_task)
        task_listbox.insert(selected_task, "✔ " + task)

    except:
        messagebox.showwarning("Warning", "Please select a task!")


title_label = tk.Label(
    root,
    text="TO-DO LIST",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=10)


task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)


add_button = tk.Button(
    root,
    text="Add Task",
    width=20,
    command=add_task
)
add_button.pack(pady=5)


task_listbox = tk.Listbox(
    root,
    width=40,
    height=15,
    font=("Arial", 12)
)
task_listbox.pack(pady=10)


complete_button = tk.Button(
    root,
    text="Mark Completed",
    width=20,
    command=mark_completed
)
complete_button.pack(pady=5)


delete_button = tk.Button(
    root,
    text="Delete Task",
    width=20,
    command=delete_task
)
delete_button.pack(pady=5)


root.mainloop()
