item1_price = float(input("Enter price of the first item: "))
item2_price = float(input("Enter price of the second item: "))
club_card = input("Does the customer have a club card? (Y/N): ")
tax_rate = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: "))
if club_card == "y" or "Y":
    if item1_price > item2_price:
        base_price = item1_price + item2_price
        discount_price = (item1_price + (item2_price/2))*.90
        total_price = discount_price + (discount_price * (tax_rate/100))
    elif item1_price < item2_price:
        base_price = item1_price + item2_price
        discount_price = (item2_price + (item1_price/2))*.90
        total_price = discount_price + (discount_price * (tax_rate/100))
elif club_card == "n" or "N":
    if item1_price > item2_price:
        base_price = item1_price + item2_price
        discount_price = (item1_price + (item2_price/2))
        total_price = discount_price + (discount_price * (tax_rate/100))
    elif item1_price < item2_price:
        base_price = item1_price + item2_price
        discount_price = (item2_price + (item1_price/2))
        total_price = discount_price + (discount_price * (tax_rate/100))
print("Base price = {:.2f}".format(base_price))
print("Price after discounts = {:.2f}".format(discount_price))
print("Total price = {:.2f}".format(total_price))
