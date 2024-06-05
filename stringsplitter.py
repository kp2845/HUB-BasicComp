string = input("Enter an odd length string: ")
if len(string) % 2 == 0:
#   print ("*** String length is:", len(string))
    print("Not an odd length string")
else:
    print("Middle character: " + string[len(string)//2])
    print("First half: " + string[0:len(string)//2])
    print("Second half: " + string[len(string)//2 +1:])
    