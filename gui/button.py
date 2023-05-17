import tkinter as tk
window=tk.Tk()
window.geometry('350x200')
l1=tk.Label(window,text="edureka!",font=("Arial Bold",12))
l1.grid(column=0,row=0)

def clicked():
    l1.configure(text="Button was clicked!")
bt=tk.Button(window,text="Enter",bg="black",fg="white",command=clicked)
bt.grid(column=10,row=2)


window.mainloop()