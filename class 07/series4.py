sum = 0
n = int (input("Enter nth Number :"))
for i in range(1,n+1):
    sum = sum + 8*i-4
    print(f"Numer of this Series: {8*i-4}")
print(f"Sum of Eight Increase : {sum}")