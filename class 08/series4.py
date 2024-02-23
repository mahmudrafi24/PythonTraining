sum = 0
n = int(input("Enter the nth Number : "))
for i in range (n+1):
    sum = sum + 8*i-4
    
print(f"Sum of 4+12+20+28+.............+{n} = {sum}")