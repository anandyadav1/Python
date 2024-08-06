def functip(gh,n):
    with open(gh,"r") as file:
        lines=file.readlines()
        sfjfj=lines[-n:]
        for i in sfjfj:
            print(i, end=" ")
gh="s.txt"
n=5
functip(gh,n)




