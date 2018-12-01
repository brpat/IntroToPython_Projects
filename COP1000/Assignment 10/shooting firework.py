
from tkinter import *
import time
import math
import random

# prepare canvas
master = Tk()

w = Canvas(master, width= 700, height= 600, bg="black")
w.pack()
def Firework():
    r= random.randrange(0, 255)
    g= random.randrange(0,255)
    b = random.randrange(0,255)
    tk_rgb ="#%02x%02x%02x" %(r, g, b)
#create x, and y position
    x = random.randrange(150, 500)
    y = random.randrange(150, 200)
    for i in range(0, 20):
        r =100
        d =math.radians(360/20*i)
        o = r * math.sin(d)
        a = r * math.cos(d)

        x3 = x + a
        y3 = y + o

        w.create_line(x, y, x3, y3, fill=tk_rgb)

      

for i in range(10):
    Firework()
    time.sleep(.3)
    w.update()
