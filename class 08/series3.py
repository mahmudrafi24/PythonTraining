sum = 0
n = int(input("Enter the n'th  number : "))
for i in range(1,n+1):
    if i%2 != 0:
        sum += i
print(f"Sum of Odd number Between 1 to {n} : {sum}")
        