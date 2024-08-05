n=int(input("Enter the any number for sequence for fibonnaci series \n"))
n1=int(input("Enter the any number for sequence for fibonnaci series of first number \n"))
n2=int(input("Enter the any number for sequence for fibonnaci series of second number \n"))
if n<0:
    print("Teke the positive number\n")
if n==1:
    print(n1)
if n==2:
    print(n2)
else:
    print("This is the series of fibonnaci nmber\n")
    print(n1,n2, end=" ")
    # print(n2)
    for i in range(3,n+1):
        n3=n1+n2
        print(n3, end=" ")
        n1=n2
        n2=n3