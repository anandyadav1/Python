def count(inputString):
    digit =0
    letter=0
    for char in inputString:
        if char.isdigit():
            digit +=1
        elif char.isalpha():
            letter+=1
    return letter,digit
def writemethod(filename,digit,letter):
    with open(filename, "w") as file:
        file.write(f"kdfsk: {letter}\n")
        file.write(f"sdmkfmsdk: {digit}\n")
inputString ="smakdf34873nfnf83743nfjeifu38484"
filename="l.txt"
letter,digit=count(inputString)
writemethod(filename,digit,letter)
