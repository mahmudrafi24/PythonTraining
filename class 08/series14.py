sum = 0
n = int(input("Enter the nth number : "))
for num in range(1,n+1):
    sum = sum + (2*num-1)*(2*num+1)*(2*num+3)*(2*num+5)
    print(f"{num}'th number of series : {num * (num +1)*(num+2)} ")
    
print(f"Sum of the series is : {sum}")