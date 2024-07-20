num= int(input("Enter the any number for armstrong:\n"))
m=num
n=num
sum=0

count =0
while(m != 0):
    m=m//10
    count +=1
print(count)

while(num != 0):
    r=num%10
    sum=sum + r**count
    num //=10

if(sum==n):
    print("Number is armstrong")
else:
    print("Number is not armstrong")
