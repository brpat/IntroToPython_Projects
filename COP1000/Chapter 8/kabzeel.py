prices = []
tax = .065















while (True):
    p = float(input("Enter a price: "))
    prices.append(p)

    for i in range(len(prices)):
        print(prices[i])

    if(prices[i] == -1):
        break;
