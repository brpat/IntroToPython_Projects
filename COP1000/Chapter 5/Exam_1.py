from tkinter import *

master = Tk()

canvas_width = 800
canvas_height = 800

w = Canvas(master, width=canvas_width,height=canvas_height, bg="blue")
w.pack()

operand1 = int(input("Enter first operand: "))
operator = str(input("Enter operator: "))
operand2 = int(input("Enter second operand: "))
result = int
sign = str 

if(operator == "+"):
    sign = "Sum"
result = operand1 + operand2
print("Result", result)

if(operator == "-"):
          sign = "Diffrence "
          result = operand1 - operand2
          print("Result", result)

if(operator == "*"):
    sign = "Product"
    result = operand1 * operand2
    print("Result", result)

if(operator == "/"):
    sign = "Quotient"
    result = operand1 / operand2
    print("Result" , result)

show = operand1 , operator, operand2, "=", result

w.create_text (canvas_width / 2, canvas_height / 2, font=("Ariel",30), text=show, fill= "red")
w.create_text(300, 300, text=sign, fill = "red", font=("Ariel", 30))

