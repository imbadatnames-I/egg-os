fib_numbers=int(input("> how meny numbers do you want to make."))
if fib_numbers<1:
    print("> That number is to small")
    fib_numbers=0
if fib_numbers>20577:
    print("> that number is to big")
    fib_numbers=0
old_fib_number=0
old_fib_number2=1
while fib_numbers>0:
    fib_number_new=old_fib_number+old_fib_number2
    print(">",fib_number_new)
    old_fib_number2=old_fib_number
    old_fib_number=fib_number_new
    fib_numbers-=1