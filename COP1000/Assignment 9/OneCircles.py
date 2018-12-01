from tkinter import *
import time
import random


master = Tk()

w = Canvas(master, width= 800, height=700, bg="#C1CAE8")
w.pack()

def oneCircle():
    x = random.randrange(150, 500)

    y = random.randrange(150, 450)

    z = random.randrange(80,255)

    r= random.randrange(0, 255)
    g= random.randrange(0,255)
    b = random.randrange(0,255)

    tk_rgb = "#%02x%02x%02x" %(r, g, b)
    


    w.create_oval(x, y, x+z, y+z, fill =tk_rgb)

for i in range(10):
    oneCircle()

#w.create_line(100, 200, 300, 400)
