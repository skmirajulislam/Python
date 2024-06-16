import tkinter as tk

var = tk.Tk()
var.geometry("655x333")

# Grid in tkinter ===:-

User = tk.Label(var,text='Username')
Password = tk.Label(var,text='Password')

#geometry management Alternate of pack
# .grid(row,coloumn)
User.grid(row=0)
Password.grid(row=1)

#variable in tkinter -> StringVar,BooleanVar,IntVar,DoubleVar 
Uservalue = tk.StringVar()
Passvalue = tk.StringVar()

#Entry class input class
#User entry or input
UserEntry = tk.Entry(var,textvariable=Uservalue)
PasswordEntry = tk.Entry(var,textvariable=Passvalue)

#.pack using alternative .grid
UserEntry.grid(row=0,column=4)
PasswordEntry.grid(row=1,column=4)

#.get takes value from entry class with in tkinter variable
#.get most importent for takeing tkinter variable value
def getdat():
    print(f"The user name is : {Uservalue.get()}")
    print(f"Password is : {Passvalue.get()}")

#button for submit data
btn = tk.Button(text='Submit',fg='Green',bg='red',command=getdat)
btn.grid(row=2,column=4)
var.mainloop()