import tkinter as tk
import sqlite3

# Connect to database
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Create table
cursor.execute(
    "CREATE TABLE IF NOT EXISTS tasks (task TEXT)"
)

# Add task
def add_task():
    task = entry.get()

    if task != "":
        cursor.execute(
            "INSERT INTO tasks VALUES (?)",
            (task,)
        )

        conn.commit()
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

# Delete task
def delete_task():
    selected = listbox.curselection()

    if selected:
        task = listbox.get(selected)

        cursor.execute(
            "DELETE FROM tasks WHERE task=?",
            (task,)
        )

        conn.commit()
        listbox.delete(selected)

# GUI window
root = tk.Tk()
root.title("Task Manager")
root.geometry("300x300")

# Entry
entry = tk.Entry(root)
entry.pack(pady=5)

# Buttons
tk.Button(root, text="Add", command=add_task).pack(pady=5)
tk.Button(root, text="Delete", command=delete_task).pack(pady=5)

# Listbox
listbox = tk.Listbox(root)
listbox.pack(pady=10, fill="both", expand=True)

# Run app
root.mainloop()