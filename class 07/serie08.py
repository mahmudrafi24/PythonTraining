sum = 0
n = int(input("Enter the nth number : "))
for i in range(1,n+1):
    sum += (2*i-1)*(2*i+1)
    print(f" {i}'th number of this Series : {(2*i-1)} * {(2*i+1)}")
print(f"Sum of this series : {sum}")