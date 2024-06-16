import tkinter as tk
from PIL import Image,ImageTk

var = tk.Tk()
var.title("Music on")

var.geometry('300x300')
var.maxsize(500,500)
var.minsize(200,200)

image = Image.open("/Users/skmirajulislam/Documents/Python/project/img/1.jpg")
photo = ImageTk.PhotoImage(image)

ldl = tk.Label(image=photo)
ldl.pack()

var.mainloop()


