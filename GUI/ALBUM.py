import tkinter as tk
from PIL import Image,ImageTk

var = tk.Tk()
var.title("Music on")
var.geometry('300x300')


image1 = Image.open("/Users/skmirajulislam/Documents/Python/project/img/1.jpg")
photo1 = ImageTk.PhotoImage(image1)
ldr = tk.Label(image=photo1)

image2 = Image.open("/Users/skmirajulislam/Documents/Python/project/img/8.jpg")
photo2 = ImageTk.PhotoImage(image2)
ldl = tk.Label(image=photo2)

ldl.pack(side="right")
ldr.pack(side='left')


var.mainloop()