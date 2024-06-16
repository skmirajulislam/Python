import tkinter as tk
from tkinter import font
import time

class DigitalClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Clock")
        self.geometry("400x200")

        self.time_label = tk.Label(self, text="", font=("Helvetica", 48), fg="white", bg="black")
        self.time_label.pack(expand=True)
        
        self.date_label = tk.Label(self, text="", font=("Helvetica", 18), fg="white", bg="black")
        self.date_label.pack(expand=True)
        
        self.update_clock()
        
    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%A, %B %d, %Y")
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        self.after(1000, self.update_clock)
        
if __name__ == "__main__":
    app = DigitalClock()
    app.configure(background='black')
    app.mainloop()
