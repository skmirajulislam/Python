import tkinter as tk

var = tk.Tk()
var.title('Attendance')
var.geometry("280x200")
var.maxsize(280,200)
var.minsize(280,200)

# Grid in tkinter ===:-

User = tk.Label(var,text='Name',relief='sunken',bg='green',fg='white')
age = tk.Label(var,text='Age',relief='sunken',bg='green',fg='white')
gen = tk.Label(var,text='Gender',relief='sunken',bg='green',fg='white')
addr = tk.Label(var,text='Address',relief='sunken',bg='green',fg='white')

#geometry management Alternate of pack
# .grid(row,coloumn)
User.grid(row=0,column=4)
age.grid(row=1,column=4)
gen.grid(row=2,column=4)
addr.grid(row=3,column=4)

#variable in tkinter -> StringVar,BooleanVar,IntVar,DoubleVar 
Uservalue = tk.StringVar()
Gender = tk.StringVar()
age = tk.StringVar()
Address= tk.StringVar()

#Entry class input class
#User entry or input
UserEntry = tk.Entry(var,textvariable=Uservalue)
ageEntry= tk.Entry(var,textvariable=age)
GenderEntry = tk.Entry(var,textvariable=Gender)
AddressEntry = tk.Entry(var,textvariable=Address)

#.pack using alternative .grid
UserEntry.grid(row=0,column=5)
ageEntry.grid(row=1,column=5)
GenderEntry.grid(row=2,column=5)
AddressEntry.grid(row=3,column=5)


#.get takes value from entry class with in tkinter variable
#.get most importent for takeing tkinter variable value
def getdat():
    file = open('data.txt','a')
    str = f'\nNAME: {Uservalue.get()}\nAGE: {age.get()}\nGENDER: {Gender.get()}\nADDRESS: {Address.get()}'
    file.write(str)
    file.close()



#button for submit data
btn = tk.Button(text='Submit',fg='Green',bg='red',command=getdat)
btn.grid(row=4,column=5)

text = tk.Label(text='Enter valid details..!').grid(row=6,column=5)

#Buttton for refresh
def exit():
    var.destroy()
button_2 = tk.Button(var,text = "Exit",command = exit)
button_2.grid(row=5,column=5)



var.mainloop()

#.place(x,y,width) alternate of grid,pack