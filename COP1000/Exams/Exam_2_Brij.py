
## Exam 2

n=9
s=n*2

for f in range(0, 10):
    s=s-2
    for f1 in range(0, f):
        print("*", end=' ')
    for f3 in range(0,s+2):
        print(" ",end=' ')
    for f2 in range(f,0,-1):
        print("*",end=' ')    
    print()
    

