def function(ands):
    with open(ands,"r") as file:
        content=file.read()
        list=','.join(content)
        print(list)

    with open(ands,"w") as file:
        file.write(list)
       


ands="j.txt"
function(ands)
