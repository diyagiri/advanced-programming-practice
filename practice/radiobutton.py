#Python Radiobutton using Application    
import tkinter as tk    
from tkinter import ttk    
win = tk.Tk()    
win.title("Python GUI App")    
#Label Creation    
ttk.Label(win, text="Choose the color:").grid(column=0,row=0)    
#Colors    
Color1='Red'    
Color2='Blue'    
Color3='Yellow'    
#Action    
def radioCall():    
   radioSel=radioVar.get()    
   if radioSel== 1:   
      win.configure(background=Color1)   
   elif radioSel== 2:  
      win.configure(background=Color2)    
   elif radioSel== 3:  
      win.configure(background=Color3)  
#Create three Radio Button    
radioVar= tk.IntVar()    
radio1=tk.Radiobutton(win, text=Color1, variable=radioVar, value=1, command=radioCall)    
radio1.grid(column=1,row=1, sticky=tk.W, columnspan=3)    
radio2=tk.Radiobutton(win, text=Color2, variable=radioVar, value=2, command=radioCall)    
radio2.grid(column=1,row=2, sticky=tk.W, columnspan=3)    
radio3=tk.Radiobutton(win, text=Color3, variable=radioVar, value=3, command=radioCall)    
radio3.grid(column=1,row=3, sticky=tk.W, columnspan=3)    

example3 = tk.Label(win, text="Bottom Row")
example3.grid(row=5, columnspan=2)
#Calling Main()    
win.mainloop() 