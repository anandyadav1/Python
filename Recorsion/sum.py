def Sum(n):
    if(n==0):
        return n
    return Sum(n-1) + n
m = int(input("Enter the value for sum \n"))
print("Sum = ", Sum(m))