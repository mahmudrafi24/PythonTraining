sum = 0
n = int (input("Enter nth Number :"))
for i in range(1,n+1):
    sum = sum + i * (i+1)
    print(f"{i}th number of this series : {i} * {(i+1)}")
print(f"Sum of 1.2+2.3+3.4+........... +{n} : {sum}")