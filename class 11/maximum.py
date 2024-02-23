def find_max(a,b,c):
    if a>=b and a>=c :
        return a
    elif b >= a and b>=c:
        return b
    else :
        return c
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))

print(f"The maximum number among {num1}, {num2}, and {num3} is : {find_max(num1,num2,num3)}")