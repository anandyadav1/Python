def Sum(n):
    if(n==0):
        return
    else:
        print(n ,end="   ")
        Sum(n-1)
m=int(input("Enter the number for print n to 1\n"))
Sum(m)