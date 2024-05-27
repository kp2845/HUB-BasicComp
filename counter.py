print("Please enter the number of coins:")
quarters = int(input("# of quarters: "))
dimes = int(input("# of dimes: "))
nickels = int(input("# of nickels: "))
pennies = int(input("# of pennies: "))
total = quarters*25 + dimes*10 + nickels*5 + pennies
dollars = round(total/100)
cents = total % 100
print("The total is " + str(dollars) + " dollars and " + str(cents) + " cents")
