sum = 0
n = int(input("Enter the nth number : "))
for num in range(1,n+1):
    sum = sum + num*num*((num+1)*(num+1))
    print(f"{num}'th number of series : {num*num*((num+1)*(num+1))} ")
    
print(f"Sum of the series is : {sum}")