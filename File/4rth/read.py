def countReadlines(fileName):
    with open(fileName, "r") as file:
        countlines=file.readlines()
    return len(countlines)
fileName="read.txt"
countlines=countReadlines(fileName)
print(f"askddjfdks {countlines}")
