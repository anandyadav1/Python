def function(filesd):
    list=[]
    with open(filesd,"r") as file:
        while True:
            lines=file.readline()
            if not lines:
                break
            list.append(lines.strip())
    return list

filesd="g.txt"
a=function(filesd)
print(a)

file2 = open("g.txt", "r")
gh=""
for line in file2:
    gh+=line
file2.close()
print(gh)
print(type(gh))


fixed=open("g.txt", "r")
j=fixed.read()
fixed.close()
print(j)