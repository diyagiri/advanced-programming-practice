import tkinter as tk
window=tk.Tk()
window.geometry('350x200')
window.title("GUI")

l1=tk.Label(window)
l1.grid(column=0,row=0)

txt=tk.Entry(window,width=10)
txt.grid(column=3,row=0)

def clicked():
    res="Wecome to "+txt.get()
    l1.configure(text=res)
bt=tk.Button(window,text="Enter",bg="black",fg="white",command=clicked)
bt.grid(column=10,row=0)
window.mainloop()