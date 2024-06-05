num_input = int(input("Please enter a positive integer greater than 1: "))
fib_number = 1
fib_number2 = 1
set_num = 3
print(fib_number)
print(fib_number2)
while set_num <= num_input:
    prt_fib_number = fib_number + fib_number2
    print(prt_fib_number)
    fib_number2 = fib_number
    fib_number = prt_fib_number
    set_num = set_num + 1
