import tkinter as tk

def add():
    a = int(entry1.get())
    b = int(entry2.get())
    result.set(a + b)

def subtract():
    a = int(entry1.get())
    b = int(entry2.get())
    result.set(a - b)

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")

root = tk.Tk()
root.title("Simple Function Buttons")
root.geometry("300x250")

tk.Label(root, text="Number 1").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Number 2").pack()
entry2 = tk.Entry(root)
entry2.pack()

result = tk.StringVar()
tk.Label(root, text="Result").pack()
tk.Entry(root, textvariable=result).pack()

tk.Button(root, text="Add", command=add).pack(pady=5)
tk.Button(root, text="Subtract", command=subtract).pack(pady=5)
tk.Button(root, text="Clear", command=clear).pack(pady=5)
tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

root.mainloop()
