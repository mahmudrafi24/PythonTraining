sum = 0
n = int (input("Enter nth Number :"))
for i in range(1,n+1):
    sum = sum + (3*i-1)*(i*2-1)
    print(f"Sum {i} this number : {(3*i-1)*(i*2-1)}")
print(f"Sum of 2.1+5.3+8.5+........... +{n} : {sum}")