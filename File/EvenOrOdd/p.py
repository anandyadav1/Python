with open("example.txt", "w") as file:
    file.write("2\n")
    file.write("3\n")
    file.write("4\n")
    file.write("5\n")
    file.write("6\n")
    file.write("7\n")
    file.write("8\n")
    file.write("9\n")
    file.write("12\n")
    file.write("22\n")
    file.write("23\n")
    file.write("27\n")
    file.write("29\n")
    file.write("28\n")

file1= open("example.txt","r")
for i in file1:
    if i.strip:
        num=int(i)
        if num%2==0:
            even=open("even.txt","a")
            even.write(str(num))
            even.write("\n")
        else:
            odd=open("odd.txt","a")
            odd.write(str(num))
            odd.write("\n")
file1.close()