rows =int(input("Enter the value for rows \n"))
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("*", end=" ")
    print()