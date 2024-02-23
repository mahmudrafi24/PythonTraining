#Taking input from the user
year = int(input("Enter a year: "))
#Checking leap year conditions
# This is a Comment
if(year % 4 == 0 and year % 100 != 0) or year %400 == 0:
    print(year," is a leap year")
else:
    print(year," is not a leap year")
    