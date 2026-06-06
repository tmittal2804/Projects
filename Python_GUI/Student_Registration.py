import tkinter as tk
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    course TEXT,
    email TEXT
)
""")

def register():
    cursor.execute(
        "INSERT INTO students (name, course, email) VALUES (?, ?, ?)",
        (entry_name.get(), entry_course.get(), entry_email.get())
    )
    conn.commit()
    label.config(text="Registered!")

root = tk.Tk()
root.title("Student Registration")
root.geometry("300x250")

entry_name = tk.Entry(root)
entry_name.pack(pady=5)

entry_course = tk.Entry(root)
entry_course.pack(pady=5)

entry_email = tk.Entry(root)
entry_email.pack(pady=5)

tk.Button(root, text="Register", command=register).pack(pady=10)

label = tk.Label(root)
label.pack()

root.mainloop()