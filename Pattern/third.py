def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(i):
            print("*", end="")
        print()

print_pattern(5)
