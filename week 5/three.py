#6
from tkinter import*

def monthly_payment():
    rate=float(entry_0.get())
    num=float(entry_1.get())
    p=float(entry_2.get())
    i=p*rate*0.01*(num//12)
    t=i+p
    m=round(t/num,2)
    payment.set(m)
    balance.set(0)

def loan():
    rate=float(entry_0.get())
    num=float(entry_1.get())
    p=float(entry_2.get()) 
    m=float(entry_3.get())
    t_p=m*num
    i=p*rate*0.01*(num//12)
    to_be=i+p
    if t_p-to_be>0:
        balance.set(0)
    else:
        balance.set(round(to_be-t_p,2))


root=Tk()

root.geometry('310x185')
root.title('tk')
label_0=Label(root, text='Annual Rate:',font=('bold',10))
label_0.place(x=2,y=5)
entry_0=Entry(root)
entry_0.place(x=180,y=5)
label_1=Label(root, text='Number of Payments:', font=('bold',10))
label_1.place(x=2,y=35)
entry_1=Entry(root)
entry_1.place(x=180,y=35)
label_2=Label(root, text='Loan Principle:', font=('bold',10))
label_2.place(x=2,y=65)
entry_2=Entry(root)
entry_2.place(x=180,y=65)
label_3=Label(root, text='Monthly Payment:', font=('bold',10))
label_3.place(x=2,y=95)
payment=StringVar()
entry_3=Entry(root, textvariable=payment)
entry_3.place(x=180,y=95)
label_4=Label(root, text='Remaining Loan:', font=('bold',10))
label_4.place(x=2,y=125)
balance=StringVar()
entry_4=Entry(root, textvariable=balance)
entry_4.place(x=180,y=125)

bt_0=Button(root, text="Find Balance", width=13, command=loan)
bt_0.place(x=5,y=155)
bt_1=Button(root, text="Monthly Payment",width=15, command=monthly_payment)
bt_1.place(x=120,y=155)
bt_2=Button(root, text="Quit", command=root.destroy)
bt_2.place(x=250,y=155)

root.mainloop()

