a = int(input("Enter the exam Number: "))
if a >= 80:
    print("Pass and Grade: A+")
elif a>=70 and a <= 79:
    print("Pass and Grade: A+")
elif a>=60 and a <= 69:
    print("Pass and Grade: A-")
elif a>=50 and a <=59:
    print("Pass and Grade: B")
elif a>=40 and a <= 49:
    print("Pass and Grade:C")
elif a>=33 and a <= 39:
    print("Pass and Grade:D")
else:
    print("Fail and Grade: F")