import tkinter as tk

#module calling
var = tk.Tk()

#for title of application
var.title("Model 1")

# Width x hight
var.geometry("200x200")
var.config(bg="cyan")

# width,height
var.maxsize(800,500)
var.minsize(200,100)

#open image
img = tk.PhotoImage(file='/Users/skmirajulislam/Documents/Python/project/img/res.png')
ldl = tk.Label(image=img).pack()

#body of page
mit = tk.Label(text="I LOVE ♥︎ PYTHON")
mit.pack()

var.mainloop()
