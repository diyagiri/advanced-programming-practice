import tkinter
window=tkinter.Tk()
window.title("GUI")
label=tkinter.Label(window, text="Hello World!").pack()
window.geometry('350x200')
#label.grid(column=0,row=0)
window.mainloop()