import tkinter as tk
var = tk.Tk()
var.geometry("655x333")

def name():
    print("Miraj")

def age():
    print(18)

def Id():
    print(3) 

def salary():
    print(19000)

frame = tk.Frame(var,borderwidth=6,bg='gray',relief='sunken')
frame.pack(side='left',anchor='nw')

b1 = tk.Button(frame,bg='black',fg='red',text='Name',command=name)
b1.pack(side='left',padx=20)

b2 = tk.Button(frame,bg='black',fg='red',text='Age',command=age)
b2.pack(side='left',padx=20)

b3 = tk.Button(frame,bg='black',fg='red',text='Id',command=Id)
b3.pack(side='left',padx=20)

b4 = tk.Button(frame,bg='black',fg='red',text='Salary',command=salary)
b4.pack(side='left',padx=20)

var.mainloop()