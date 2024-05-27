print("Please enter the number of coins:")
quarters = input("# of quarters: ")
dimes = input("# of dimes: ")
nickels = input("# of nickels: ")
pennies = input("# of pennies: ")
total = float(quarters)*25 + float(dimes)*10 + float(nickels)*5 + float(pennies)*1
#print(total)
dollars = round(total/100)
cents = total % 100
#format(cents, '2')
print("The total is " + str(dollars) + " dollars and " + str(cents) + " cents")
