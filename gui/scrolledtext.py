import tkinter as tk
from tkinter import scrolledtext
window=tk.Tk()
window.geometry('350x200')
window.title("GUI") 

l1=tk.Label(window,text="Scrolled Text Example",font=("Times New Roman",15),bg="green",fg="white")
l1.grid(column=0,row=0)

txt=scrolledtext.ScrolledText(window,width=40,height=10,font=("Times New Roman", 15)) 
txt.grid(column = 0, pady = 10, padx = 10)

txt.focus()
window.mainloop()