a = int(input("Enter the First Number : "))
b = int(input("Enter the Second Number :"))
c = int(input("Enter the Third Number : ")) 
if a>b:
    if a>c:
        if b>c:
            print(b)
        else:
            print(c)
    else:
        print(a)
else:
    if b>c:
        if a>c:
            print(a)
        else:
            print(c)
    else:
        print(b)
        
'''
This series of nested if-else statements checks which of the three numbers is the largest and second-largest, and then prints the second-largest number.

The outermost if statement checks if a is greater than b.

If true, it further checks if a is greater than c.

If this condition is true, it checks if b is greater than c.

If b is greater than c, it prints b as the second-largest.

If b is not greater than c, it prints c as the second-largest.

If the initial condition (a > c) is false, it prints a as the largest.

If the outermost condition (a > b) is false, it goes to the else block and checks if b > c.

If true, it checks if a > c, and prints a if true, otherwise prints c.

If b is not greater than c, it prints b as the second-largest.
'''   