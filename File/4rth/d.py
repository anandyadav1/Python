def function(digit):
    userInput= input("Enter stringg eith number \n")
    with open(digit, "w") as file:
        file.write(userInput)
def functions(digit):
    with open(digit, "r") as file:
        content=file.read()
    words=content.split()
    digits=[word for word in words if word.isdigit()]
    for i in digits:
        print(i)
digit="d.txt"
function(digit)
functions(digit)

