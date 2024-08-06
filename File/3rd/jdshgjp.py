def functionName(files,n):
    with open(files, "r") as file:
        for i in range(n):
            lists=file.readline()
            if not lists:
                break
            print(lists, end=" ")
files="s.txt"
n=5
functionName(files,n)


def append(g, text):
    with open(g,"a") as file:
        file.write(text+'\n')
g="s.txt"
text="snfksjgksjgkokrgorg"
append(g,text)

def readd(m):
    with open(m,"r") as file:
        t=file.read()
    return t
m="s.txt"
a=readd(m)
print(a)



