sum = 0
n = int(input("Enter the n'th number : "))
for i in range(1,n+1):
    num = i * (i + 1)
    sum = sum + num
    print(f"Number of Series: {num}")

print(f"Sum of Series: {sum}")