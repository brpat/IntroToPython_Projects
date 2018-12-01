##Assignment 8



no=0
cnt=0
counter = 0
subtotal = 1
tax = 0.06
i=0
no=int(input("Enter total no of items $: "))
   
prices=[0]*no
while(cnt < no):
    price = float(input("Enter the price of the item $: "))
    subtotal += price
    tax = subtotal * 0.065
    total = subtotal + tax
    prices[cnt]=price
    cnt = cnt + 1
    

    
for i in range(len(prices)):
    print( prices[i]  )
print ("Total: ",total )
print ("Tax: $",tax )


while(True):
    p = float(input("Enter a price" ))

    prices.append(p)

  

print("Wal-Mart".center(60))
print("1521 W Granada Blvd".center(60))
print("Ormond Beach , FL".center(60))
print("(386) 672-2104".center( 60))
print("Manager - Chuck Norris".center(60))
  

print("Subtotal         $:   ", locale.currency(subtotal))
print("Tax              $:   ", locale.currency(tax))
print("Total            $:   ", locale.currency(subtotal + tax))
print("Your total is : ", locale.currency(total))

print("Thank you for shopping at your local Wal-Mart".center(60, "~"))




