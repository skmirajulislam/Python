from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title('Wether X')
root.geometry("900x500+300+200")
root.resizable(False,False)


def getWether():
    try:
        city=textfeild.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude) # type: ignore
        print(result)

        home = pytz.timezone(result) # type: ignore
        local_time = datetime.now(home)
        current_time =local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WETHER")

        #wether Api 
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=646824f2b7b86caffec1d0b16ea77f79"

        json_data = requests.get(api).json()
        condition=json_data['weather'][0]['main'] 
        description=json_data['weather'][0]["description"] 
        temp = int(json_data['main']['temp']-273.15) 
        pressure = json_data['main']['pressure'] 
        humidity = json_data['main']['humidity'] 
        wind = json_data['wind']['speed'] 

        t.config(text=(temp,'º')) # type: ignore
        c.config(text=(condition,'|','FEELS','LIKE',temp,'º')) # type: ignore

        W.config(text=wind) # type: ignore
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    
    except Exception as e:
        messagebox.showerror("Weather App"," Invalid entry..!")
    
    finally:
        print("Connection Establish")



#dark to light

#646824f2b7b86caffec1d0b16ea77f79 API KEY
#search box
search_img=PhotoImage(file="Guitkinter/img/search.png")
myimg=Label(image=search_img)
myimg.place(x=20,y=20)

textfeild=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfeild.place(x=50,y=40)
textfeild.focus()

search_icon=PhotoImage(file="Guitkinter/img/search_icon.png")
myimg_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",fg="white",command=getWether)
myimg_icon.place(x=400,y=34)

#logo
logo_img=PhotoImage(file="Guitkinter/img/logo.png")
logo=Label(image=logo_img)
logo.place(x=150,y=100)

#Button box
frame_image=PhotoImage(file="Guitkinter/img/box.png")
frame_myimg=Label(image=frame_image)
frame_myimg.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15))
c.place(x=400,y=250)

W=Label(text="...",font=("arial",20,"bold"),fg="#1ab5ef")
W.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),fg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),fg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"),fg="#1ab5ef")
p.place(x=670,y=430)

#root.attributes('-alpha',0.5)
root.mainloop()