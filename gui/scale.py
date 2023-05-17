import tkinter as tk
from tkinter import CENTER, HORIZONTAL, messagebox
root= tk.Tk()

root.title('Scale Demo')

root.geometry("200x200")

def slide():
    msg = messagebox.showinfo( "GUI Event Demo",v.get())

v = tk.DoubleVar()
scale = tk.Scale( root, variable = v, from_ = 1, to = 50, orient = HORIZONTAL)
scale.pack(anchor=CENTER)

btn = tk.Button(root, text="Value", command=slide)
btn.pack(anchor=CENTER)

root.mainloop()