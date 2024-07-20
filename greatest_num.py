a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))

if(a>=b and a>=c):
    print("first number is largest:",a)
elif(b>=c):
    print("second number is largest:",b)
else:
    print("third number is largest:",c)


num=int(input("enter the any number:"))
if(num%7==0):
    print("number is divided by 7")
else:
    print("Number is not divided by 7")