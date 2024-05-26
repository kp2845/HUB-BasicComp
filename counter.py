print("Please enter the number of coins:")
print("# of quarters:")
quarters = input()
quarters = float(quarters)
print("# of dimes:")
dimes = input()
dimes = float(dimes)
print("# of nickels:")
nickels = input()
nickels = float(nickels)
print("# of pennies:")
pennies = input()
pennies = float(pennies)
total = float(quarters)*.25 + float(dimes)*.10 + float(nickels)*.05 + float(pennies)*.01
dollars = total/1.0
cents = total % 1.0
print("The total is" + dollars + "and" + cents + "cents")
