prices = []
tax = .065


while (True):
    p = float(input("Enter a price: "))
    prices.append(p)

    for i in range(len(prices)):
        print(prices[i])

    if(prices[i] == -1):
        break;

print("Subtotal is ", sum(prices))
tax = sum(prices)*.065
print(" Your tax amount is ", tax)
total = tax + sum(prices)
print("Your total is: ", total)

