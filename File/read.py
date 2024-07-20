with open("demo.txt", "r") as f:
    # data = f.read()
    # print(data)
    # print(type(data))
    line1= f.readline()
    print(line1)
    line2 = f.readline()
    print(line2)

with open("demo.txt", "a") as f:
    f.write("\nThen I'll move to Cyber Security")
    f.close()