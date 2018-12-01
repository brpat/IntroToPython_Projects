from tkinter import*

master = Tk()

canvas_width = 800
canvas_height = 800

w = Canvas(master, width=800 , height= canvas_height)


w.pack()
# comment      x1 y1   x2  y2    

w.create_line(0, 100, 300, 100, fill= "#CF1D58",)
            
w.create_line(0, 100, 500, 600, fill= "#476042",width=5, )

w.create_rectangle(200, 400, 600, 530, fill= "#0AD5F5", outline ="blue" ,width = 5)

w.create_polygon (100, 400 , 400,  350, 700, 400, fill= "green")

w.create_oval(400,400,300,500, fill="yellow", outline= "red", width=5)

coord = 510, 260, 400, 300 

w.create_arc(coord, start= 60, extent=120 , fill = "red")

w.create_text(500,500, text = "Daytona State College", fill = "purple")

img = PhotoImage(file= "images.gif")
w.create_image(10,400, anchor=NW, image =img)
