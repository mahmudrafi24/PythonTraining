n = int(input('Enter Number : '))
sum = 0
for i in range(1,n+1):
    sum = sum + (i*2-1)
    print(f"{i}th number of series : {i*2-1}")
print(f"Sum of 1 to {n} is {sum}")