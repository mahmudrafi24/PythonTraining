def add_num(a,b):
    return a + b
def sub_num(a,b):
    return a - b
def mul_num(a,b):
    return a * b
def div_num(a,b):
    return a / b
num1 = int(input("Enter the first Number : "))
num2 = int(input("Enter the second Number : "))
print(f"Sum of {num1} and {num2} is  = {add_num(num1,num2)}")
print(f"Sub of {num1} and {num2} is = {sub_num(num1,num2)}")
print(f"mul of {num1} and {num2} is = {mul_num(num1,num2)}")
print(f"div of {num1} and {num2} is = {div_num(num1,num2)}")