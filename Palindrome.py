n=int(input("Enter the any number \n"))
m=n
s=0
while n>0:
    r=n%10
    s=s*10+r
    n//=10
if m==s:
    print("This number is palindrome number /n")
else:
    print("This number is not palindrome number\n")

