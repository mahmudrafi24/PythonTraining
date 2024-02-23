num = int(input("Enter the number : "))
if num < 0:
    print("Factorial does not exist")
elif num == 0:
    print(f"Factorial for {num}  = 1")
else:
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    print(f"Factorial for {num} = {fact}")