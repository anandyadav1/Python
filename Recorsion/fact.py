def Fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return Fact(n-1) * n

m= int(input("Enter the any value for factorial:\n"))
print("Factorial = ",Fact(m))