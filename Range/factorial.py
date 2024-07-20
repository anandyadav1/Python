num = int(input("enter the any number for factorial\n"))

fact = 1
for el in range(1, num+1):
    fact *=el

print("Factorial of",num, "= ", fact)