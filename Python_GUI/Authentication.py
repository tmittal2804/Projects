import tkinter as tk
import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
)
""")

# Signup function
def signup():
    cursor.execute(
        "INSERT INTO users VALUES (?, ?)",
        (entry_user.get(), entry_pass.get())
    )

    conn.commit()
    label.config(text="Signup Success")

# Login function
def login():
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (entry_user.get(), entry_pass.get())
    )

    if cursor.fetchone():
        label.config(text="Login Success")
    else:
        label.config(text="Invalid")

# GUI window
root = tk.Tk()
root.title("Login System")
root.geometry("300x200")

# Inputs
entry_user = tk.Entry(root)
entry_user.pack(pady=5)

entry_pass = tk.Entry(root, show="*")
entry_pass.pack(pady=5)

# Buttons
tk.Button(root, text="Signup", command=signup).pack(pady=5)

tk.Button(root, text="Login", command=login).pack(pady=5)

# Output label
label = tk.Label(root)
label.pack()

# Run app
root.mainloop()