sum = 0
n = int (input("Enter nth Number :"))
for i in range(1,n+1):
    sum = sum + 3*i-1
    print(f"Number of this Series : {3*i-1}")
print(f"Sum of Three Increase : {sum}")