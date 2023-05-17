import tkinter as tk
window=tk.Tk()
window.geometry('350x200')
window.title("GUI")

rad1=tk.Radiobutton(window,text="Python",value=1)
rad2=tk.Radiobutton(window,text="Java",value=2)
rad3=tk.Radiobutton(window,text="Scala",value=3)
rad1.grid(column=0,row=0)
rad2.grid(column=1,row=0)
rad3.grid(column=2,row=0)

window.mainloop()