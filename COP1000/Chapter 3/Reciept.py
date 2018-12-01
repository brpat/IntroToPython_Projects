##x =10   x=20.5  x= 

print("                 ABC Reciept      ")
print("============================================")

apple = int(input("Enter amount for Apple:   "))

pen = int(input("Enter amount for Pen:      "))

mouse = int(input("Enter amount for Mouse:   "))

paper = int(input("Enter amount for Paper:   "))

# create three more variables

subtotal =int(apple + pen + mouse + paper)

tax = int(subtotal * 0.065)

total = int(subtotal + tax)



print("                 ABC Reciept")
print("=============================================")

print("Apple                             $", apple,".00")
print("Pen                               $ ", pen,".00") 
print("Mouse                             $", mouse,".00")
print("Paper                             $", paper,".00")

print("=============================================")
print("Subtotal                          $",subtotal,".00" )
print("Tax                               $ ",tax,".00" )
print("Total                             $",total,".00")

print(" Thank   You   For   Your   Business ")




