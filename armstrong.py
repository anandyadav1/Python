n=int(input("Enter the number for any number\n"))
m=n
o=n
s=0
i=0
while o>0:
    o//=10
    i+=1
print(i)
while n>0:
    r=n%10
    s+=r**i
    n//=10
if m==s:
    print("Armstrong number \n")
else:
    print("Not armstrong number")
