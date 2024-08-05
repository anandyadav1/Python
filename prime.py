n=int(input("Enter the any number for prime number\n"))
flag=True
if n==1:
    print("this number: ", n, "is not a prime number\n")
elif n==2:
    print("this number: ", n, "is a prime number\n")
else:
    for i in range(2, n):
        if n%i==0:
            flag =False
            break
    if flag==False:
        print("this number: ", n, "is not a prime number\n")
    else:
        print("this number: ", n, "is a prime number\n")


