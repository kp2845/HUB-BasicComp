char = input("Enter a character: ")
if char.islower():
    print(char + " is a lower case letter.")
elif char.isupper():
    print(char + " is a an upper case letter.")
elif char.isdigit():
    print(char + " is a digit.")
elif char.isascii():
    print(char + " is a non-alphanumeric character.")
