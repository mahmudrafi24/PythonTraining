sum = 0
n = int(input("Enter the nth number : "))
for num in range(1,n+1):
    sum = sum + num ** 2
    print(f"{num}'th number of series : {num**2} ")
    
print(f"Sum of the series is : {sum}")