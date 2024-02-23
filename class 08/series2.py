sum = 0
n = int(input("Enter the n'th Number : "))
for i in range(1,n+1):
    if i%2 == 0:
        sum += i
print(f"Sum of Even number Between 1 to {n} : {sum}")
