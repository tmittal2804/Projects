import tkinter as tk
from math import sqrt

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("350x500")

expression = ""

def press(value):
    global expression
    expression += str(value)
    screen.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        history.insert(tk.END, expression + " = " + result)
        screen.set(result)
        expression = result
    except:
        screen.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    screen.set("")

def square_root():
    global expression
    try:
        result = str(sqrt(float(screen.get())))
        history.insert(tk.END, "√" + screen.get() + " = " + result)
        screen.set(result)
        expression = result
    except:
        screen.set("Error")

screen = tk.StringVar()

entry = tk.Entry(
    root,
    textvar=screen,
    font=("Arial",20),
    justify="right"
)
entry.pack(fill="x", padx=10, pady=10)

buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    
    for btn in row:
        action = equal if btn=="=" else lambda x=btn: press(x)
        
        tk.Button(
            frame,
            text=btn,
            width=6,
            height=2,
            command=action
        ).pack(side="left", padx=2, pady=2)

tk.Button(root,text="√",command=square_root,width=10).pack(pady=5)
tk.Button(root,text="Clear",command=clear,width=10).pack(pady=5)

tk.Label(root,text="History").pack()

history = tk.Listbox(root,height=8)
history.pack(fill="both",expand=True,padx=10,pady=10)

root.mainloop()