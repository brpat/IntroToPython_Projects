
##a = [0]*5
##
##print(a)
##
##print(a[2])
##
##a[0]= 5
##print(a)
##a[2]=10
##print(a)
##
##a[4]="hello"
##print(a)
##
##print(a[-5])


a1 = [2, 5, 6, 9, 6, 4, 3, 3, 5]
print(a1)

for i in range(4):
    a1[i]+=3

print(a1[3:7])

a2 = [3, 3, 3]

a3 = a1 + a2

print(a3)

if (3 in a1):
    print("3 is in the list")
print(len(a3))

##a3[12] = 20
a3.append(20)
print(a3)

del a3[3]
print(a3)

a3.extend(a2)
print(a3)


#insert increase list size
a3.insert(4, 100)    
print(a3)
print(len(a3))

# assignment replace the value

a3[4]=200
print(a3)
print(len(a3))

b = "hello"

print(b[0])

print(max(a3))
print(min(a3))

a3.pop(4)

a3.reverse()
print(a3)

a3.sort()
print(a3)

a3.sort(reverse=True)
print(a3)

a4 = ['b', 'c', 'f', 'a', 'x']

a4.sort(reverse=True)
print(a4)


print(sum(a1))


