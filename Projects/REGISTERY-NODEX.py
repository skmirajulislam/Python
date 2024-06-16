import tkinter as tk

var = tk.Tk()
var.title('Attendance')
var.geometry("280x200")
var.maxsize(280, 200)
var.minsize(280, 200)

# Labels
User = tk.Label(var, text='Name', relief='sunken', bg='green', fg='white')
age_label = tk.Label(var, text='Age', relief='sunken', bg='green', fg='white')
gen = tk.Label(var, text='Gender', relief='sunken', bg='green', fg='white')
addr = tk.Label(var, text='Address', relief='sunken', bg='green', fg='white')

User.grid(row=0, column=4)
age_label.grid(row=1, column=4)
gen.grid(row=2, column=4)
addr.grid(row=3, column=4)

# StringVars
Uservalue = tk.StringVar()
Gender = tk.StringVar()
age_value = tk.StringVar()
Address = tk.StringVar()

# Entry Widgets
UserEntry = tk.Entry(var, textvariable=Uservalue)
ageEntry = tk.Entry(var, textvariable=age_value)
GenderEntry = tk.Entry(var, textvariable=Gender)
AddressEntry = tk.Entry(var, textvariable=Address)

UserEntry.grid(row=0, column=5)
ageEntry.grid(row=1, column=5)
GenderEntry.grid(row=2, column=5)
AddressEntry.grid(row=3, column=5)

# Function to save data to file
def save_data():
    data_string = f'\nNAME: {Uservalue.get()}\nAGE: {age_value.get()}\nGENDER: {Gender.get()}\nADDRESS: {Address.get()}'
    with open('data.txt', 'a') as file:
        file.write(data_string)

    # Update the message label
    text.config(text='Data saved successfully!')

# Submit Button
btn = tk.Button(text='Submit', fg='Green', bg='red', command=save_data)
btn.grid(row=4, column=5)

# Message Label
text = tk.Label(text='Enter valid details..!')
text.grid(row=6, column=5)

# Exit Button
def exit():
    var.destroy()

button_2 = tk.Button(var, text="Exit", command=exit)
button_2.grid(row=5, column=5)

var.mainloop()
