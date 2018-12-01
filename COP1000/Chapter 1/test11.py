# Today is chapter 1 lesson, we work on canvas
from tkinter import *
import time

master = Tk()

canvas_width = 800
canvas_height = 700

w = Canvas (master, width=800, height=canvas_height)

w.pack()

img = PhotoImage(file ="images.gif")
pic1= w.create_image(10, 400, anchor=NW, image=img)
pic2=w.create_image(10,100,anchor=NW, image=img)

w.update()


w.move(pic1, 20, -20)
w.move(pic2, 20,20)
time.sleep(1)
w.update()

w.move(pic1,30,-40)
w.move(pic2,20,20)
time.sleep(1)
w.update










