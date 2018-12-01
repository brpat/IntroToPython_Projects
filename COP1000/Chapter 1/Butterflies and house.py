from tkinter import*
import time
master = Tk()

canvas_width = 800
canvas_height = 800

w = Canvas(master, width=800 , height= canvas_height)


w.pack()
# comment      x1 y1   x2  y2    

            


w.create_rectangle(200, 400, 600, 530, fill= "#0AD5F5", outline ="blue" ,width = 5)

w.create_rectangle(210, 420, 400 , 500, fill= "#DE4D1D", outline = "black", width = 3)

w.create_rectangle(210,500,300, 460, fill = "yellow" , outline = "black" , width = 3)

w.create_rectangle(210,420,300, 460, fill = "green" , outline = "black",  width = 3)

w.create_rectangle(400,420, 300,465, fill = "red" , outline = "black" , width = 3 )

w.create_rectangle(600, 340 , 530, 400 , fill = "brown" , outline = "blue")

w.create_rectangle(590, 410, 510, 530 , fill = "grey" , outline = "black")

w.create_oval(290,200, 100,100 , fill = "gold" , outline = "black")

w.create_oval(545,495,515,470 ,fill= "yellow", outline = "red", width=5)            

w.create_polygon (100, 400 , 400,  350, 700, 400, fill= "black")

coord = 510, 260, 400, 300 

w.create_text(550,450, text = "201", fill = "purple")


img=PhotoImage(file="butterfly2.gif")
pic1 = w.create_image(10,400,anchor=NW, image= img)

pic2 = w.create_image(10,100,anchor=NW, image= img)

w.update()

w.move(pic1, 20, -20)
w.move(pic2, 20, 20)
time.sleep(.75)
w.update()

w.move(pic1, 30, -40)
w.move(pic2, 20, 20)
time.sleep(.75)
w.update()

w.move(pic1, 40, -50)
w.move(pic2, 20, 20)
time.sleep(.75)
w.update()

w.move(pic1, 50, -60)
w.move(pic2, 20, 20)
time.sleep(.75)
w.update()

w.move(pic1, 50, -80)
w.move(pic2, 20, 20)
time.sleep(.75)
w.update()

w.move(pic1, 50, -40)
w.move(pic2, 20, 20)
time.sleep(.75)
w.update()

w.move(pic1, 50, 20)
w.move(pic2, 20,-40)
time.sleep(.75)
w.update()

w.move(pic1, 50, 20)
w.move(pic2, 20,-40)
time.sleep(.75)
w.update()

w.move(pic1, 30, 20)
w.move(pic2, 30,-40)
time.sleep(.75)
w.update()

w.move(pic1, 20, 20)
w.move(pic2, 40,-40)
time.sleep(.75)
w.update()

w.move(pic1, 20,-40)
w.move(pic2, 30, 40)
time.sleep(.75)
w.update()

w.move(pic1, 20, 20)
w.move(pic2, 20, 40)
time.sleep(.75)
w.update()

w.move(pic1, 20, 40)
w.move(pic2, 20, 40)
time.sleep(.75)
w.update()

w.move(pic1, 30, 20)
w.move(pic2, 20,-40)
time.sleep(.75)
w.update()

w.move(pic1, 30, 20)
w.move(pic2, 20,-40)
time.sleep(.75)
w.update()

w.move(pic1, 20, -20)
w.move(pic2, 45, 30)
time.sleep(.75)
w.update()

w.move(pic1, 30, 20)
w.move(pic2, 45,-40)
time.sleep(.75)
w.update()

w.move(pic1, 30, 20)
w.move(pic2, 45,-40)
time.sleep(.75)
w.update()

w.move(pic1, 30, 20)
w.move(pic2, 45,40)
time.sleep(.75)
w.update()

w.move(pic1, 10, -20)
w.move(pic2, 40, 40)
time.sleep(.75)
w.update()

w.move(pic1, 30, -20)
w.move(pic2, 40, 40)
time.sleep(.75)
w.update()

w.move(pic1, 30, -20)
w.move(pic2, 40, 0)
time.sleep(.75)
w.update()

w.move(pic1, 30, 20)
w.move(pic2, 40, 0)
time.sleep(.75)
w.update()


