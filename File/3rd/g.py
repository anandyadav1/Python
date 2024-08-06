def readfile(filename):
    list =[]
    with open(filename, "r") as file:
        while True:
            line =file.readline()
            if not line:
                break
            list.append(line.strip())
    return list

filename="g.txt"
a=readfile(filename)
print(a)

