import tkinter as tk
var = tk.Tk()
var.geometry("655x333")

#frame of exist root
#Frames == :-

f1 = tk.Frame(var,bg='gray',borderwidth=6,relief='sunken')
f1.pack(side='left',fill='y')

f2 = tk.Frame(var,bg='gray',borderwidth=6,relief='sunken')
f2.pack(side='top',fill='x')

#for use frame we use label inside it
#Labels == :-

l1 = tk.Label(f1,text="Side bar",relief='raised',bg='red',fg='black')
l1.pack(pady=130,padx=40)

l2 = tk.Label(f2,text="Tool ber",relief='raised',bg='orange',fg='black')
l2.pack()

var.mainloop()