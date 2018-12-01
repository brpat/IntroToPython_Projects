
##Reciept version 2
##User can enter as many prices as needed, 
##show subtotal, tax, total 
##- you create a while to take prices, 
##While (true):
##-stop the loop:
##while(True):
##     price = input()
##	if (price = -1):
##	  break



import locale
locale.setlocale(locale.LC_ALL, '' )



print("Wal-Mart".center(60))
print("1521 W Granada Blvd".center(60))
print("Ormond Beach , FL".center(60))
print("(386) 672-2104".center( 60))
print("Manager - Chuck Norris".center(60))

counter = 0
subtotal = 1
tax = 0.06

while (True):
    counter += 1
    price = float(input("Enter the price of the item $: "))
    subtotal += price
    tax = subtotal * 0.065
    total = subtotal + tax
    if (price == -1):
        break;
    
    
print("Subtotal         $:   ", locale.currency(subtotal))
print("Tax              $:   ", locale.currency(tax))
print("Total            $:   ", locale.currency(subtotal + tax))
print("Your total is : ", locale.currency(total))

print("Thank you for shopping at your local Wal-Mart".center(60, "~"))
