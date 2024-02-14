sum=0
n=int(input("enter the nth number: "))
for i in range (1,n+1):
    sum=sum+i*(1*i+1)*(1*i+1)
print(f"sum of the series1*3*5*7+3*5*7*9+5*7*9*11...........+{n} {sum})    