import turtle
import colorsys
t=turtle.Turtle()
w=turtle.Screen()
w.bgcolor("black")
t.speed(1)
h=0
c=colorsys.hsv_to_rgb(h,1,1)

def orange():
    t.fillcolor("dark orange")
    t.begin_fill()
    t.pu()
    t.goto(-100,100)
    t.pd()
    t.fd(300)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(300)
    t.rt(90)
    t.fd(50)
    t.pu()
    t.end_fill()

def white():
    t.fillcolor("white")
    t.begin_fill()
    t.goto(-100,50)
    t.pd()
    t.rt(90)
    t.fd(300)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(300)
    t.rt(90)
    t.fd(50)
    t.pu()
    t.end_fill()

def green():
    t.fillcolor("green")
    t.begin_fill()
    t.goto(-100,0)
    t.pd()
    t.rt(90)
    t.fd(300)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(300)
    t.rt(90)
    t.fd(50)
    t.pu()
    t.end_fill()

def circle():
    t.goto(60,25)
    t.pd()
    t.pensize(2)
    t.circle(20)
    t.pu()

def ashok():
    t.goto(40,25)
    t.pd()
    t.pencolor("blue")
    t.pensize(2)
    for i in range(24):
        t.fd(20)
        t.bk(20)
        t.lt(15)
    t.pu()

def wish():
    t.goto(-260,200)
    t.color('darkorange') 
    t.write("I am", font=("algerian", 40, "bold")) 
    t.goto(-100,180)
    t.color('white') 
    t.write("Proud to", font=("edwardian script itc", 40, "bold")) 
    t.goto(50,200)
    t.color('green') 
    t.write("Be a indian", font=("edwardian script itc", 40, "bold")) 

def coll():
    t.pu()
    t.goto(-300,-200)
    t.pd()
    t.color('peru') 
    t.write(" HAPPY REPUBALIC DAY ", font=("algerian", 40, "bold"))
    t.pu()



orange()
white()
green()
circle()
ashok()   
wish()
coll()



