# Write a program that asks the user to enter an amount of
# money in the format of dollars and remaining cents.
# The program should calculate and print the minimum number
# of coins (quarters, dimes, nickels and pennies) that are equivalent to the given amount.

dollars = int(input("Please enter how many dollars: "))
cents = int(input("Please enter how many cents: "))
total = dollars*100 + cents
quarters = (total // 25)
print(str(quarters) + " quarters")
remainder1 = total % 25
dimes = remainder1 // 10
print(str(dimes) + " dimes")
remainder2 = remainder1 % 10
nickels = remainder2 // 5
print(str(nickels) + " nickels")
remainder3 = remainder2 % 5
pennies = remainder3
print(str(pennies) + " pennies")
