prices = []
tax = .065


print("Wal-Mart".center(60))
print("1521 W Granada Blvd".center(60))
print("Ormond Beach , FL".center(60))
print("(386) 672-2104".center( 60))
print("Manager - Chuck Norland".center(60))
  



while (True):
    p = float(input("Enter a price: "))
    prices.append(p)

    for i in range(len(prices)):
        if(prices[i] != -1):
            print("Item",i+1,"      :",prices[i])

    if(prices[i] == -1):
        break;

print("Subtotal is $", sum(prices))
tax = sum(prices)*.065
print(" Your tax amount is $", tax)
total = tax + sum(prices)
print("Your total is: $", total)




