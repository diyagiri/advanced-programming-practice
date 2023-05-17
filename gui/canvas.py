import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
#window.geometry('200x200')

C = tk.Canvas(window, bg = "black", height = 250, width = 300)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start = 0, extent = 150, fill = "white")
line = C.create_line(10,10,200,200,width=8,fill = 'red')
C.pack()

window.mainloop()