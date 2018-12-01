from tkinter import*

master = Tk()

canvas_width = 800
canvas_height = 700

w = Canvas(master, width=canvas_width , height=canvas_height, bg="#B7F9E3")
w.pack()

w.create_line(0,0, 150,150 , fill= "blue" )
w.pack
# comment 

w.create_rectangle(60, 90, 200, 260, fill= "red")


w.create_line(200,320, 400, 450 , fill="green" ,width=5)

w.create_polygon(252, 122, 560, 40 , 720, 260, 510 , 380 , 190 , 340, fill= "orange")
