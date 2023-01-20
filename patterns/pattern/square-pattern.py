def printSquare(n):
    if n > 20:
        return "Please input a valid integer between 1 to 20"
    
    for i in range(0, n):
        for j in range(0, n):
            print("* ", end="")
        print()

    return "Square Pattern Printed Successfully"



result = printSquare(4)
print(result)
