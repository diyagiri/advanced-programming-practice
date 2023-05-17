import tkinter as tk
window=tk.Tk()
window.geometry('350x200')
window.title("GUI")

check_1 = tk.IntVar()
check_2 = tk.IntVar()
check_3 = tk.IntVar()
 
def check1Clicked():
    if check_1.get() :
        print('Checkbox 1 selected')
    else :
        print('Checkbox 1 unselected')
 
def check2Clicked():
    if check_2.get() :
        print('Checkbox 2 selected')
    else :
        print('Checkbox 2 unselected')
 
def check3Clicked():
    if check_3.get() :
        print('Checkbox 3 selected')
    else :
        print('Checkbox 3 unselected')
 
check_but_1 = tk.Checkbutton(window, text = 'Listening to Music', variable = check_1,
                onvalue = 1, offvalue = 0, command=check1Clicked)
check_but_1.pack()
 
check_but_2 = tk.Checkbutton(window, text = 'Reading Books', variable = check_2,
                onvalue = 1, offvalue = 0, command=check2Clicked)
check_but_2.pack()
 
check_but_3 = tk.Checkbutton(window, text = 'Watching Movies', variable = check_3,
                onvalue = 1, offvalue = 0, command=check3Clicked)
check_but_3.pack()
 
window.mainloop()