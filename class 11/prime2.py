num = int(input("Enter a number : "))
flag = True
if num >1:
    for i in range(2,num+1):
        if num %i == 0:
            flag = False
            break
    if flag:
        print("It's a prime number")
    else :
        print("It's not a prime number")
else:
    print("It's not a prime number")