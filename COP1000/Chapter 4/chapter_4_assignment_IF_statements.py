a= int(input("Enter first number: "))
b= int(input("Enter second number:"))
c= int(input("Enter third number:"))
d= int(input("Enter fourth number:"))

if((a < b) and (a < c) and (a < d)) :
   print(a, " is smallest")

if ((b < a) and (b < c) and (b < d)) :
    print(b, " is smallest")

if((c < a) and (c < b) and (c < d)) :
    print(c, " is smallest")

if((d < a) and ( d < b) and (d < c)):
    print(d, " is smallest") 
