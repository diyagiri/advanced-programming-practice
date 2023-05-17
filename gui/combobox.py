import tkinter as tk
from tkinter import ttk
window=tk.Tk()
window.geometry('350x200')
combo=ttk.Combobox(window)
combo['values']=(1,2,3,4,5,"Text")
combo.current(4)
combo.grid(column=0,row=0)
window.mainloop()