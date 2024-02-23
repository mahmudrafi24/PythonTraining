a = int(input("Enter the 1st Number : "))
b = int(input("Enter the 2nd Number : "))
c = int(input("Enter the 3rd Number : "))
if a>b:
    if a>c:
        print("Maximum number : ",a)
    else:
        print("Minimum number : ",c)
else:
    if b>c:
        print("Maximum number : ",b)
    else:
        print("Minimum number : ",c)