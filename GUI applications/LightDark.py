import tkinter as t

window = t.Tk()
window.title("Theme Changer")
window.geometry("600x800")
window.config(bg="white")


on = t.PhotoImage(file="Guitkinter/img/light.png")
off = t.PhotoImage(file="Guitkinter/img/dark.png")

button_mode = True

def toggle():

	global button_mode
	if button_mode == True:
		button.config(image=off, bg="#26242f",activebackground="#26242f") 
		window.config(bg="#26242f")
		button_mode = False

	else:
		button.config(image=on, bg="white",activebackground="white")
		window.config(bg="white")
		button_mode = True


button = t.Button(window, image=on,bd=0, bg="white",activebackground="white",command=toggle)
button.pack(padx=50, pady=50)

window.mainloop()
