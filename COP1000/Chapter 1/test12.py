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










## comment     x1  y1   x2   y2         
##w.create_line(0, 100, 300, 100, fill="DarkCyan", )
##w.create_line(10, 300,20, 100, 500, 600, fill="#476042",width=5, smooth="true" )

##w.create_rectangle (60, 60, 200, 230, fill="yellow", outline="blue",width=5)


##w.create_polygon (300, 100, 350, 200, 230, 300,180, 350, 100, 100, 80, 50, fill="green")


##w.create_oval(400, 400 ,300, 500, fill="yellow", outline="blue",width=5 )


##coord = 510, 260, 150, 300

##w.create_arc(coord, start= 60, extent= 120, fill = "red")


##w.create_text(500,500, text="Daytona State College", fill= "blue")


