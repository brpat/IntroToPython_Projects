
smallno=0
n=0
while (True):
    ##    counter =c 1
    n = int(input("Enter the number: "))
    if(smallno > n):
        smallno=n
        
    if (n == -1):
        break;
  
    
print("Smallest number is",smallno)
