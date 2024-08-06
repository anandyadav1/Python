file = open("m.txt", "w+")
l =["sgjfd\n", "SJHDGJUSH\n", "dsjgdf\n", "sjghjf\n"]
d="sdfjds\n"
file.writelines(l)
file.close()

file1 =open("m.txt", "r")
print(file1.read())
file.close()